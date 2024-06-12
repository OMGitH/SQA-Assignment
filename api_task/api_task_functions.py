import textwrap
import requests
from api_task_test_data import video_file_extension, year_start_photos, year_start_videos, number_of_photos, number_of_videos, year_end_photos, year_end_videos


def get_request(url):
    response_full = requests.get(url)
    response_content_encoded = response_full.json()
    return response_full, response_content_encoded


def extract_photos_or_videos_from_response(response_content_dict):
    photos_or_videos = response_content_dict["collection"]["items"]
    return photos_or_videos


def check_status_code_and_photos_or_videos_number(response_full, response_content_encoded, photos_or_videos):
    if photos_or_videos == "photos":
        expected_number_of_photos_or_videos = number_of_photos
    elif photos_or_videos == "videos":
        expected_number_of_photos_or_videos = number_of_videos
    else:
        raise ValueError(f"Provided value '{photos_or_videos}' for parameter 'photos_or_videos' is incorrect. Correct values are 'photos' or 'videos'.")
    # Check response status code.
    response_status_code = response_full.status_code
    assert response_full.status_code == requests.codes.ok, f"Execution stopped: {photos_or_videos.capitalize()} response status code ({response_status_code}) is different from expected status code ({requests.codes.ok})."
    print(f"\n\n{photos_or_videos.capitalize()} assertion part:")
    print(f"Assertion passed: {photos_or_videos.capitalize()} response status code ({response_status_code}) is the same as expected status code ({requests.codes.ok}).")

    # Check number of returned photos or videos.
    response_number_of_photos_or_videos = len(response_content_encoded["collection"]["items"])
    assert response_number_of_photos_or_videos == expected_number_of_photos_or_videos, f"Execution stopped: Obtained number of {photos_or_videos} ({response_number_of_photos_or_videos}) is different from expected number of {photos_or_videos} ({expected_number_of_photos_or_videos})."
    print(f"Assertion passed: Obtained number of {photos_or_videos} ({response_number_of_photos_or_videos}) equals to expected number of {photos_or_videos} ({expected_number_of_photos_or_videos}).")


def extract_photos_data(photos):
    selected_photos_data = {}
    for index, photo in enumerate(photos, 1):
        photo_name = f"Photo {index}"
        selected_photos_data[photo_name] = {}
        selected_photos_data[photo_name]["title"] = photo["data"][0]["title"]
        # Extract creation date without time part.
        selected_photos_data[photo_name]["creation_date"] = photo["data"][0]["date_created"].split("T")[0]

        selected_photos_data[photo_name]["description"] = photo["data"][0]["description"]
        selected_photos_data[photo_name]["link"] = photo["links"][0]["href"]
        selected_photos_data[photo_name]["type"] = photo["links"][0]["rel"]
    return selected_photos_data


def extract_videos_data(videos):
    selected_videos_data = {}
    for index, video in enumerate(videos, 1):
        video_name = f"Video {index}"
        selected_videos_data[video_name] = {}
        selected_videos_data[video_name]["title"] = video["data"][0]["title"]
        media_files_url = video["href"]
        _, all_media_files_links = get_request(media_files_url)
        selected_videos_data[video_name]["all_video_files_links"] = []
        for file_link in all_media_files_links:
            if file_link.split(".")[-1] == video_file_extension:
                selected_videos_data[video_name]["all_video_files_links"].append(file_link)
    return selected_videos_data


def check_photos_creation_year(selected_photos_data):
    year_start_photos_range = int(year_start_photos)
    year_end_photos_range = int(year_end_photos)
    for photo in selected_photos_data.keys():
        # Extract year from creation_date.
        creation_year = int(selected_photos_data[photo]["creation_date"].split("-")[0])

        assert creation_year in range(year_start_photos_range, year_end_photos_range + 1), f"Execution stopped: Creation year ({creation_year}) of photo '{photo}: {selected_photos_data[photo]["title"]}' is not within chosen years range ({year_start_photos_range} - {year_end_photos_range})."
        print(f"Assertion passed: Creation year ({creation_year}) of photo '{photo}: {selected_photos_data[photo]["title"]}' is within chosen years range ({year_start_photos_range} - {year_end_photos_range}).")


def print_photos_data(selected_photos_data):
    print("\nPhotos information part:")
    if year_start_photos == year_end_photos:
        print(f"{number_of_photos} photos taken in {year_start_photos} showing surface of Mars:")
    else:
        print(f"{number_of_photos} photos taken between years {year_start_photos} - {year_end_photos} showing surface of Mars:")
    for photo in selected_photos_data.keys():
        print(f"\n\t{photo} information:")
        print(f"\t\tPhoto title:\n\t\t{selected_photos_data[photo]["title"]}")
        print(f"\n\t\tPhoto creation date:\n\t\t{selected_photos_data[photo]["creation_date"]}")
        print(textwrap.fill(f"\n\tPhoto description:\n\t{selected_photos_data[photo]["description"]}", 200, subsequent_indent="\t\t", replace_whitespace=False))
        print(f"\n\t\tPhoto {selected_photos_data[photo]["type"]} can be found at:\n\t\t{selected_photos_data[photo]["link"]}")


def print_videos_data(selected_videos_data):
    print("\nVideos information part:")
    if year_start_videos == year_end_videos:
        print(f"Link to every video file for first {number_of_videos} videos taken in {year_start_videos}:")
    else:
        print(f"Link to every video file for first {number_of_videos} videos taken between years {year_start_videos} - {year_end_videos}:")
    for video in selected_videos_data.keys():
        print(f"\n\t{video} '{selected_videos_data[video]["title"]}' all video files links:")
        for video_file_link in selected_videos_data[video]["all_video_files_links"]:
            print(f"\t{video_file_link}")

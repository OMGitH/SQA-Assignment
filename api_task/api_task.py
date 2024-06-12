from api_task_functions import get_request, extract_photos_or_videos_from_response, print_photos_data, print_videos_data, extract_photos_data, extract_videos_data, check_status_code_and_photos_or_videos_number, check_photos_creation_year
from api_task_test_data import url_photos, url_videos

# Getting and printing data for 5 photos taken in 2018 with visible Mars surface. There are also few assertions performed.
photos_response_full, photos_response_content_dict = get_request(url_photos)
check_status_code_and_photos_or_videos_number(photos_response_full, photos_response_content_dict, "photos")
photos = extract_photos_or_videos_from_response(photos_response_content_dict)
selected_photos_data = extract_photos_data(photos)
check_photos_creation_year(selected_photos_data)
print_photos_data(selected_photos_data)

# Getting and printing all video files links for first 5 videos from 2018 regarding Mars. There are also few assertions performed.
videos_response_full, videos_response_content_dict = get_request(url_videos)
check_status_code_and_photos_or_videos_number(videos_response_full, videos_response_content_dict, "videos")
videos = extract_photos_or_videos_from_response(videos_response_content_dict)
selected_videos_data = extract_videos_data(videos)
print_videos_data(selected_videos_data)

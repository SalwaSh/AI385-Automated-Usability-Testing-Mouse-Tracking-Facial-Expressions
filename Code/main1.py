from utilities.mouse_tracking import track_user_path
from utilities.generate_screenshot import generate_user_path
from utilities.task_usability import compute_similarity_mouse_tracking_based
from utilities.DB_utilities import insert_mouse_similarity


track_user_path()
generate_user_path()
result = compute_similarity_mouse_tracking_based()
insert_mouse_similarity(result)
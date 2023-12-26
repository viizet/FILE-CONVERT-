import os
import asyncio
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

async def fix_thumb(thumb, max_width=320, max_height=320):
    try:
        if thumb is not None:
            img = Image.open(thumb)
            img.thumbnail((max_width, max_height))  # Resize within the specified dimensions
            img.save(thumb, "JPEG")
            width, height = img.size
            return width, height, thumb
    except Exception as e:
        print(e)
        return None, None, None
    
async def take_screen_shot(video_file, output_directory, ttl):
    out_put_file_name = f"{output_directory}/{time.time()}.jpg"
    file_genertor_command = [
        "ffmpeg",
        "-ss",
        str(ttl),
        "-i",
        video_file,
        "-vframes",
        "1",
        out_put_file_name
    ]
    process = await asyncio.create_subprocess_exec(
        *file_genertor_command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    return None

# Example usage
thumbnail_path = "path/to/thumbnail.jpg"
video_path = "path/to/video.mp4"
output_directory = "path/to/output"
max_width, max_height = 320, 320  # Desired maximum width and height

thumbnail_width, thumbnail_height, resized_thumbnail = asyncio.run(fix_thumb(thumbnail_path, max_width, max_height))

if resized_thumbnail:
    screenshot_path = asyncio.run(take_screen_shot(video_path, output_directory, ttl=5))
    if screenshot_path:
        print(f"Thumbnail Size: {thumbnail_width}x{thumbnail_height}")
        print(f"Resized Thumbnail Path: {resized_thumbnail}")
        print(f"Screenshot Path: {screenshot_path}")
    else:
        print("Failed to capture screenshot.")
else:
    print("Failed to process thumbnail.")

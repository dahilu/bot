from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, MediaGroup

from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_photo_id(m: types.Message):
    await m.answer(m.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_video_id(m: types.Message):
    await m.answer(m.video.file_id)

@dp.message_handler(Command('get_cat'))
async def send_photo_cat(m:types.Message):
    photo_id = 'AgACAgQAAxkBAAIBdmEcGCFbWEViG9jNnqObwJTcqMkXAAK5qzEbuvi9UqKtCFKBbwh7AQADAgADdwADIAQ'
    photo_url= "https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/cat_relaxing_on_patio_other/1800x1200_cat_relaxing_on_patio_other.jpg"
    photo_bytes = InputFile(path_or_bytesio="c:\\temp\\cat.jpg")

    await bot.send_photo(chat_id=m.from_user.id, photo=photo_id, caption="Get photo /get_more_cats")

@dp.message_handler(Command('get_more_cats'))
async def send_photo_cats(m:types.Message):
    album = MediaGroup()
    photo_id = 'AgACAgQAAxkBAAIBdmEcGCFbWEViG9jNnqObwJTcqMkXAAK5qzEbuvi9UqKtCFKBbwh7AQADAgADdwADIAQ'
    photo_url= "https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/cat_relaxing_on_patio_other/1800x1200_cat_relaxing_on_patio_other.jpg"
    photo_bytes = InputFile(path_or_bytesio="c:\\temp\\cat.jpg")
    video_id = 'BAACAgIAAxkBAAIBeGEcGE4PLebi6TSCY4WBI6PIlP7KAAKHEgACoL3hSE8PFNHrBLwLIAQ'

    album.attach_photo(photo_id)
    album.attach_photo(photo_url)
    album.attach_photo(photo_bytes)
    album.attach_video(video_id)

    await m.answer_media_group(album)

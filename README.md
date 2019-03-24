# image_tools

**Overview:**

I required some images to be resized but I can't get used to the photo tools Mac provides. Decided to create a script that resizes images. You provide the url, it resizes it to your specifications and returns it from memory. Simple and gets the job done. Resizes png and jpg/jpeg.

Uses Django for backend. Images are not saved to database. They are resized in memory and pushed to user for download from there, hence not very scalable.

For safety, uses Django csrf middleware to prevent cross-site request forgery.

Available here: www.therewecode.com/image-tools

**For next time:**
1. Update CSS. It's not scalable and not very mobile-friendly.
2. I just made this for myself, but if others were to use it, I would provide more instructions to the user.
3. Create some request restrictions. As mentioned earlier, it does everything in memory and there's nothing to prevent the user from going crazy with requests (or a bot).

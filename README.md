# URL Content Fetcher — Terminal Style Scraper

Hey there! This is a **Python script** that works right in your terminal. It lets you enter a URL, fetch the content (like a webpage), and saves it to a file — **on repeat**. Great for learning how `requests` works, or just grabbing HTML/text from pages.

---

## What It Does (In Simple Words)

> **Step 1:** You type in a URL (like `https://example.com`)  
> **Step 2:** You type in a file name (like `page.html`)  
> **Step 3:** It grabs the stuff (HTML/text) from that page  
> **Step 4:** Saves it into the file  
> **Step 5:** Waits 4 seconds... clears the screen... and asks again!

It’s like a looped mini-scraper that never gets tired.

---

## Demo Preview

```bash
Enter your URL: https://example.com
Enter your file name like text.txt, text.html etc: saved.html
<!doctype html>
<html>
  <head>...</head>
  <body>...</body>
</html>
Your result: saved.html

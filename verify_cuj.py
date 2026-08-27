from playwright.sync_api import sync_playwright

def run_cuj(page):
    page.goto("http://localhost:8000")
    page.wait_for_timeout(1000)

    # We need to simulate uploading a file using the input element directly.
    # The frontend hides the input, but playwright can interact with it.
    file_input = page.locator("#file-input")

    # Upload requirements.txt to trigger the analysis
    file_input.set_input_files("backend/requirements.txt")

    page.wait_for_timeout(2000) # Wait for upload and analysis to start

    # Wait for the results to appear (the summary text should become visible)
    page.wait_for_selector("#res-summary", state="visible", timeout=10000)
    page.wait_for_timeout(1000)

    # Take screenshot at the key moment
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(2000)  # Hold final state for the video

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()  # MUST close context to save the video
            browser.close()

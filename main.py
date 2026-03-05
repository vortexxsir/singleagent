# -*- coding: utf-8 -*-
# 🚀 PHOENIX V100.44 (SECRET-ONLY)
# 🛡️ BY PRAVEERFUCKS | 100-AGENT BURST
# ⚡ FIX: ZERO SIGNATURE | RAW SECRET INJECTION

import os, time, sys, string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

TABS_PER_MACHINE = 5 
PURGE_INTERVAL = 120 

def get_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.page_load_strategy = 'eager'
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_experimental_option("mobileEmulation", {"deviceName": "iPad Pro"})
    return webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

def launch_strike(driver, target, raw_message):
    """Deploys the JS Engine using ONLY the secret text."""
    for i in range(TABS_PER_MACHINE):
        driver.execute_script(f"window.open('https://www.instagram.com/direct/t/{target}/', '_blank');")
        time.sleep(5) 

    handles = driver.window_handles[1:]
    
    for handle in handles:
        driver.switch_to.window(handle)
        driver.execute_script("""
            const secretText = arguments[0];
            window.strikeInterval = setInterval(() => {
                const box = document.querySelector('div[role="textbox"], [contenteditable="true"]');
                if (box) {
                    box.focus();
                    // ⚡ INJECTS RAW SECRET TEXT
                    document.execCommand('insertText', false, secretText);
                    box.dispatchEvent(new Event('input', { bubbles: true }));
                    
                    const enter = new KeyboardEvent('keydown', { 
                        bubbles: true, key: 'Enter', code: 'Enter', keyCode: 13 
                    });
                    box.dispatchEvent(enter);
                    
                    setTimeout(() => { box.innerHTML = ""; }, 1);
                }
            }, 15); // High-speed pulse
        """, raw_message)

def main():
    cookie = os.environ.get("INSTA_COOKIE")
    target = os.environ.get("TARGET_THREAD_ID")
    # Pulls the exact text from your GitHub Secret named 'MESSAGES'
    raw_message = os.environ.get("MESSAGES")

    if not raw_message:
        print("❌ ERROR: 'MESSAGES' secret is empty!")
        return

    driver = get_driver()
    try:
        driver.get("https://www.instagram.com/")
        driver.add_cookie({'name': 'sessionid', 'value': cookie.strip(), 'domain': '.instagram.com'})
        
        while True:
            launch_strike(driver, target, raw_message)
            time.sleep(PURGE_INTERVAL)
            
            # ♻️ PURGE SESSION
            curr_handles = driver.window_handles
            for i in range(1, len(curr_handles)):
                driver.switch_to.window(curr_handles[i])
                driver.close()
            driver.switch_to.window(curr_handles[0])
            driver.refresh()
            time.sleep(5)

    except Exception as e:
        print(f"⚠️ REBOOTING: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

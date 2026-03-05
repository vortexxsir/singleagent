# -*- coding: utf-8 -*-
# 🚀 PHOENIX V100.43 (AUTO-PURGE)
# 🛡️ BY PRAVEERFUCKS | ZERO-LAG STRIKE
# ⚡ FIX: 120s MEMORY PURGE | DOM BLOAT PROTECTION

import os, time, random, sys, string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

TABS_PER_MACHINE = 5 
PURGE_INTERVAL = 120 # 🔥 HARD RESET every 2 minutes to stop lag

def get_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.page_load_strategy = 'eager'
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_experimental_option("mobileEmulation", {"deviceName": "iPad Pro"})
    
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(options=options, service=service)

def launch_strike(driver, target, signature):
    """Deploys the JS Engine into fresh tabs."""
    # 1. Open Tabs
    for i in range(TABS_PER_MACHINE):
        driver.execute_script(f"window.open('https://www.instagram.com/direct/t/{target}/', '_blank');")
        time.sleep(5) 

    handles = driver.window_handles[1:]
    
    # 2. Inject JS Engine
    for handle in handles:
        driver.switch_to.window(handle)
        driver.execute_script("""
            const payloadText = arguments[0];
            window.strikeInterval = setInterval(() => {
                const box = document.querySelector('div[role="textbox"], [contenteditable="true"]');
                if (box) {
                    const salt = Math.random().toString(36).substring(5);
                    box.focus();
                    document.execCommand('insertText', false, payloadText + " [" + salt + "]");
                    box.dispatchEvent(new Event('input', { bubbles: true }));
                    const enter = new KeyboardEvent('keydown', { bubbles: true, key: 'Enter', code: 'Enter', keyCode: 13 });
                    box.dispatchEvent(enter);
                    setTimeout(() => { box.innerHTML = ""; }, 1);
                }
            }, 10);
        """, signature)

def main():
    cookie = os.environ.get("INSTA_COOKIE")
    target = os.environ.get("TARGET_THREAD_ID")
    signature = "😅🔥 SAMMY/ANDH KE HATER Sꪖꪗ |-LOF!! /~ 𝐃ᴀᴅ𝐘🥀"

    driver = get_driver()
    try:
        # Initial Login
        driver.get("https://www.instagram.com/")
        driver.add_cookie({'name': 'sessionid', 'value': cookie.strip(), 'domain': '.instagram.com'})
        
        while True:
            print("🚀 INITIALIZING FRESH STRIKE...")
            launch_strike(driver, target, signature)
            
            # 🔥 THE PURGE TIMER
            time.sleep(PURGE_INTERVAL)
            
            print("♻️ MEMORY PURGE: CLEANING DOM BLOAT...")
            # Close all tabs except the first one to free RAM
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

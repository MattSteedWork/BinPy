import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pickle
from prettytable import PrettyTable
import yaml

GTFO_DATA_FILE = 'gtfobins_data.pkl'
GTFO_BASE_URL = 'https://gtfobins.github.io'
GTFO_SEARCH_URL = GTFO_BASE_URL + '/#'

def display_help():
    print("GTFOBins CLI Tool")
    print("--------------------------")
    print("This command line tool allows you to search and display GTFOBins entries.")
    print("\nCommands:")
    print("  help   - Show this help message")
    print("  clear  - Clear the screen")
    print("  exit   - Exit the tool")
    print("\nUsage:")
    print("Enter a search term, such as 'sudo', to find GTFOBins entries")
    print("To use a command, type the command name and press Enter.")
    print("\nExample:")
    print("Search GTFObins: sudo")

def download_entries():
    response = requests.get(GTFO_SEARCH_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    entries = {}
    
    for entry in soup.select('a[href*="/gtfobins/"]'):
        link = urljoin(GTFO_BASE_URL, entry['href'])
        title = entry.text.strip()
        entries[title] = link
    
    with open(GTFO_DATA_FILE, 'wb') as f:
        pickle.dump(entries, f)
    
    return entries

def load_entries():
    if not os.path.exists(GTFO_DATA_FILE):
        return download_entries()
    
    with open(GTFO_DATA_FILE, 'rb') as f:
        return pickle.load(f)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_entries(entries, query):
    results = {}
    
    for title, link in entries.items():
        if query.lower() in title.lower():
            results[title] = link
    
    return results

def display_entry_content(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    functions = soup.select('h2.function-name')
    if not functions:
        print("No functions found.")
        return
    
    terminal_width = os.get_terminal_size().columns
    max_width = int(terminal_width * 0.3)
    
    for function in functions:
        function_name = function.text.strip()
        
        description_element = function.find_next_sibling('p')
        if description_element:
            description = description_element.text.strip()
        else:
            description = "No description available"
        
        ul_element = function.find_next_sibling('ul')
        if ul_element:
            examples = ul_element.select('li')
        else:
            examples = []
        
        if not examples:
            print("No examples available.")
            return
        
        table = PrettyTable()
        table.field_names = ['Function', 'Description', 'Code']
        table.align['Function'] = 'l'
        table.align['Description'] = 'l'
        table.align['Code'] = 'l'
        table.border = True
        table.hrules = 1
        table.vrules = 1
        table.max_width = max_width
        
        for example in examples:
            code = example.find('code').get_text()
            table.add_row([function_name, description, code])
        
        print(table)
        print("\n")

        
def banner():
	print("""\033[1;32;40m
 ▄▄▄▄    ██▓ ███▄    █       ██▓███  ▓██   ██▓
▓█████▄ ▓██▒ ██ ▀█   █      ▓██░  ██▒ ▒██  ██▒
▒██▒ ▄██▒██▒▓██  ▀█ ██▒     ▓██░ ██▓▒  ▒██ ██░
▒██░█▀  ░██░▓██▒  ▐▌██▒     ▒██▄█▓▒ ▒  ░ ▐██▓░
░▓█  ▀█▓░██░▒██░   ▓██░ ██▓ ▒██▒ ░  ░  ░ ██▒▓░
░▒▓███▀▒░▓  ░ ▒░   ▒ ▒  ▒▓▒ ▒▓▒░ ░  ░   ██▒▒▒ 
▒░▒   ░  ▒ ░░ ░░   ░ ▒░ ░▒  ░▒ ░      ▓██ ░▒░ 
 ░    ░  ▒ ░   ░   ░ ░  ░   ░░        ▒ ▒ ░░  
 ░       ░           ░   ░            ░ ░     
      ░                  ░            ░ ░     
	""")

def main():
    gtfo_entries = load_entries()

    while True:
        clear_screen()
        banner()
        print("\033[1;31;40mType 'help' for more information")
        query = input("\033[1;36;40mSearch GTFObins: ")

        if query.lower() == 'exit':
           break
        elif query.lower() == 'clear':
            clear_screen()
            continue
        elif query.lower() == 'help':
            display_help()
            input("\nPress Enter to continue.")
            continue

        results = search_entries(gtfo_entries, query)

        if not results:
            print("No results found.")
        else:
            for title, link in results.items():
                print(f"{title}: {link}\n")
                display_entry_content(link)

        input("\nPress Enter to continue \033[1;31;40m(Type 'exit' at the prompt to quit.)")

if __name__ == '__main__':
    main()



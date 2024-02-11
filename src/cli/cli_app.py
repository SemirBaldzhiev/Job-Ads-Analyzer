from src.user.user import User
from getpass import getpass
from src.analysis.job_analysis import *
from src.analysis.company_analysis import *
from src.dbsqlite.db_worker import get_all_job_data, get_all_company_data, get_full_data, get_user_skills

class CLIApp:    
    def __init__(self):
        self.current_user = None
    
    def menu(self) -> None:
        '''
        Print menu for the CLI
        '''
        print("Commands:")
        print("1.  Login")
        print("2.  Register")
        print("3.  Job Ads WordCloud By Title")
        print("4.  Filter by different criteria")
        print("5.  Sort by different criteria")
        print("6.  Distribution by date posted")
        print("7.  Distribution by count ads")
        print("8.  Company distribution by date founded")
        print("9.  Display job data in terminal")
        print("10. Display company data in terminal")
        print("11. Display full data job ads and companies in terminal")   
        print("12. Recommend jobs")
        print("13. Change password")
        print("14. Close the program")
        print("To use commands from 3 to 6 you shoud be logged in")
        
    def print_heading(self) -> None:
        '''
        Print heading for the CLI
        '''
        print("=====================================================")
        print("=========Welcome to the Job Ads Analyzer CLI=========")
        print("=====================================================")
        self.menu()
        print("-------To continue, please login or register!--------")
        

    def login_cmd(self) -> None:
        '''
        Login command for the CLI
        '''
        while (True):
            input_username = input("Username: ")
            input_password = getpass("Password: ")
            if User.valid_credentials(input_username, input_password):
                print("Sucessful login!")
                print(f"Welcome back, {input_username}!")
                self.current_user = input_username
                break
            else:
                print("Incorect username or password! Please try again!")
                exit = input("Do you want to exit login (yes/no)? ")
                if exit.lower() == "yes":
                    break
    def register_cmd(self) -> None:
        '''
        Register command for the CLI
        '''
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = getpass("Enter password: ")
        skills = input("Enter your skills separated by comma: ")
        
        new_user = User(first_name, last_name, username,email, password, skills)
        new_user.save()
        self.current_user = username

    def filter_cmd(self):
        '''
        Filter command for the CLI
        '''
        filter_criteria = input("Enter filter criteria in the format <key=\"value\"> exp: title=\"София\": ")
        filter_criteria = filter_criteria.split(", ")
        kwargs = {filter.split("=")[0]: filter.split("=")[1] for filter in filter_criteria}
        print(kwargs)
        filtered_data = filter_job_ads(**kwargs)
        print(filtered_data)

    def sort_cmd(self):
        '''
        Sort command for the CLI
        '''
        while (True):
            input_order = input("Enter order ascending/descending: ")
            if input_order.lower() == "ascending" or input_order.lower() == "descending":
                break
            else:
                print("Invalid order! Please try again!")
                
        columns_sorted =  input("Enter columns to be sorted by: ")
        data = get_full_data()
        order_asc = True
        if input_order == "descending":
            order_asc = False
        sorted_data = sort_ads(data, order_asc, columns_sorted)
        print(sorted_data)

    def recommend_jobs_cmd(self):
        '''
        Recommend jobs for the current logged in user
        '''
        
        user_skills = get_user_skills(self.current_user)
        print(user_skills)
        recommended_jobs = remomend_job(user_skills[0].split(","))
        print(recommended_jobs)
    
    def change_password_cmd(self):
        '''
        Change password for the current logged in user
        '''
        old_password = getpass("Enter old password: ")
        new_password = getpass("Enter new password: ")
        user = User.get_user(self.current_user)
        if user.change_password(old_password, new_password):
            print("Password changed successfully!")
        else:
            print("Password change failed! Please try again!")
    
    def display_job_data_in_terminal(self):
        '''
        Display job data in terminal
        '''
        data = get_all_job_data()
        print(data)
    
    def display_company_data_in_terminal(self):
        '''
        Display company data in terminal
        '''
        data = get_all_company_data()
        print(data)
    
    def display_full_data(self):
        '''
        Display full data job ads and companies in terminal
        '''
        data = get_full_data()
        print(data)
    
    def run(self):
        '''
        Run all commands intercatively
        '''
        self.print_heading()
        while(True):
            input_cmd = input("Enter command number: ")
            
            if input_cmd == "":
                continue
            
            if input_cmd.isnumeric() == False:
                print("Please enter a valid command number!")
                continue
            else:
                cmd_num = int(input_cmd)
            
            try:
                if cmd_num == 1:
                    if self.current_user != None:
                        print("You are already logged in!")
                    else:
                        self.login_cmd()
                elif cmd_num == 2:
                    if self.current_user != None:
                        print("You are already registered!")
                    else:
                        self.register_cmd()
                elif self.current_user != None:
                    if cmd_num == 3:
                            wordcloud_job_titles()
                    elif cmd_num == 4:
                            self.filter_cmd()
                    elif cmd_num == 5:
                            self.sort_cmd()
                    elif cmd_num == 6: 
                            distribution_by_date_posted()
                    elif cmd_num == 7:
                            distribution_by_cnt_ads()
                    elif cmd_num == 8:
                            distribution_by_date_founded()
                    elif cmd_num == 9:
                            self.display_job_data_in_terminal()
                    elif cmd_num == 10:
                            self.display_company_data_in_terminal()
                    elif cmd_num == 11:

                            self.display_full_data()
                    elif cmd_num == 12:
                            self.recommend_jobs_cmd()
                    elif cmd_num == 12:
                            self.change_password_cmd()
                    elif cmd_num == 13:
                        break
                    else:
                        print("Invalid command number! Please try again!")
                else:
                    print("Plaese login or register before using this command!")
            except Exception:
                print("Something went wrong! Please try again!")
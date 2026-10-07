import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer():
    def __init__(self):
        self.data=None
    def load_data(self,file_path):
        
        self.data=pd.read_csv(file_path,encoding='latin1')
        print("data load succesfully")
        print(self.data)
  
        
    def explore_data(self):
        while True:
            print("1.Display the first 5 rows")
            print("2.display the last 5 rows")
            print("3.display the columns name")
            print("4.display data types")
            print("5.dipslay basic info")
            choice2=int(input("enter the choice......"))
            match choice2:
                case 1:
                    print("-----------------------------------------")
                    print("these are the first  5 values of dataset")
                    print(self.data.head())
                    print("-----------------------------------------")
                    
                case 2:
                    print("-----------------------------------------")
                    print("these are the last 5 values of dataset")
                    print(self.data.tail())
                    print("-----------------------------------------")
                case 3:
                    print("-----------------------------------------")
                    print("this are the all columns name ")
                    print(self.data.columns)
                    print("-----------------------------------------")
                case 4:
                    print("-----------------------------------------")
                    print("datatypes.....")
                    print(self.data.dtypes)
                    print("-----------------------------------------")
                case 5:
                    print("-----------------------------------------")
                    print("basic info")
                    print(self.data.info())
                    print("-----------------------------------------")
    def clean_data(self):
        while True:
            print("=====Handle Missing Values=====")
            print("1.Display rows with missing values")
            print("2.Fill missing values with mean")
            print("3.Drop rows with missing values")
            print("4.Replace missing values with a specific value")
            print("5.Go to main menu")
            choice3=int(input("enter the choice...."))
            match choice3:
                case 1:
                    print("null values in all columns")
                    print(self.data.isna().sum())
                case 2:
                    print("fill null values with mean succesfully....")
                    self.data.fillna(self.data["quantity"].mean(),inplace=True)  
                    print(self.data.info())
                case 3:
                    print("succesfully drop rows with null valuesn")
                    clean_df=self.data.dropna()
                    print(clean_df.info())
                case 4:
                    print("before fill values ")
                    print(self.data.info())
                    print("sucessfullt changes missing value with unknown value....")
                    self.data.fillna("Unknown_value",inplace=True) 
                    print("after filling values ")    
                    print(self.data.info())     
                case 5:
                    break                           
                    
                
                    
    def mathematical_operations(self):
        print(self.data["profit"]+1000)
        
    def combine_data(self,df2):
        merge_pd=pd.merge(self.data,df2,how="outer")
        return merge_pd
        
        
    def split_data():
        print("")
    def search_sort_filter(self):
        while True:
            print("1.search")
            print("2.sort")
            print("3.filter")
            print("4.go to main menu")
            choice4=int(input("enter the choice "))
            match choice4:
                case 1:
                  id=int(input("enter the order id for search"))
                  
                  result=self.data[self.data["order_id"]==id]
                  if result.empty:
                    print("data found")
                    print("order id not found")
                  else:
                    print(result)
                case 2:
                    while True:
                        print("1.acending")
                        print("2.decending")
                        print("go to main menu")
                        choice5=int(input("enter the order id for search"))
                        match choice5:
                            case 1:
                                column_name=input("enter the column name for sort the dataset  ")
                                sort_data=self.data.sort_values(by=column_name,ascending=True)
                                print(sort_data)
                            case 2:
                                column_name=input("enter the column name for sort the dataset  ")
                                sort_data=self.data.sort_values(by=column_name,ascending=False)
                                print(sort_data)
                            case 3:
                                break
                                
    def aggregate_functions(self):
        while True:
            print("1.revenue")
            print("2.profit")
            print("3.discounted_price")
            print("4.shipping_cost")
            print("5.rating")
            print("6.quantity")
            print("7.discounted_price")
            print("8.product_price")
            print("9.go to main menu")
            choice3=int(input("enter the choice"))
            match choice3:
                case 1:
                    print(self.data["revenue"].agg(["sum","max","min"]))
                case 2:
                    print(self.data["profit"].agg(["sum","max","min"]))
                    
                case 3:
                    print(self.data["discounted_price"].agg(["sum","max","min"]))
                case 4:
                    print(self.data["shipping_cost"].agg(["sum","max","min"]))       
                case 5:
                    print(self.data["rating"].agg(["sum","max","min"]))           
                case 6:
                    print(self.data["quantity"].agg(["sum","max","min"]))              
                case 7:
                    print(self.data["discounted_price"].agg(["sum","max","min"]))     
                case 8:
                    print(self.data["product_price"].agg(["sum","max","min"]))
                case 9:
                    break
                   
            
    def statistical_analysis(self):
        while True:
                    print("1.revenue")
                    print("2.profit")
                    print("3.discounted_price")
                    print("4.shipping_cost")
                    print("5.rating")
                    print("6.quantity")
                    print("7.discounted_price")
                    print("8.product_price")
                    print("9.go to main menu")
                    choice3=int(input("enter the choice"))
                    match choice3:
                        case 1:
                            print(self.data["revenue"].agg(["mean","median","std","var"]))
                        case 2:
                            print(self.data["profit"].agg(["mean","median","std","var"]))
                            
                        case 3:
                            print(self.data["discounted_price"].agg(["mean","median","std","var"]))
                        case 4:
                            print(self.data["shipping_cost"].agg(["mean","median","std","var"]))       
                        case 5:
                            print(self.data["rating"].agg(["mean","median","std","var"]))           
                        case 6:
                            print(self.data["quantity"].agg(["mean","median","std","var"]))              
                        case 7:
                            print(self.data["discounted_price"].agg(["mean","median","std","var"]))     
                        case 8:
                            print(self.data["product_price"].agg(["mean","median","std","var"]))
                        case 9:
                            break
        
    def create_pivot_table(self):
        
        index_name=input("enter the index for pivot tha dataset")
        column_name=input("enter the column name for pivot the dataset")
        valuess=input("enter the values for pivot the dataset")
        print("mean,median,std,var,sum")
        agg_func=input("enter the aggegate function for pivot the dataset")
        new_df=pd.pivot_table(data=self.data,index=index_name,columns=column_name,values=valuess,aggfunc=agg_func)    
        print(new_df)    
    def visualize_data(self):
        while True:
            print("1.barplot")
            print("2.lineplot")
            print("3.scatterplt")
            print("4.pieplot")
            print("5.histogram")
            print("6.stackplot")
            print("7.subplot")
            print("8.go to main menu")
            choice6=int(input("enter the choice"))
            match choice6:
               case 1:
                 x_column = input("Enter the X column name: ")
                 y_column = input("Enter the Y column name: ")

                 plt.bar(
                     self.data[x_column],
                     self.data[y_column],
                     color="skyblue"
                 )

                 plt.title(f"{y_column} by {x_column}")
                 plt.xlabel(x_column)
                 plt.ylabel(y_column)

                 plt.xticks(rotation=45)
                 plt.tight_layout()
                 plt.show()


               case 2:
                   x_column = input("Enter the X column name: ")
                   y_column = input("Enter the Y column name: ")

                   plt.plot(
                       self.data[x_column],
                       self.data[y_column],
                       color="green",
                       marker="o"
                   )

                   plt.title(f"{y_column} vs {x_column}")
                   plt.xlabel(x_column)
                   plt.ylabel(y_column)

                   plt.xticks(rotation=45)
                   plt.tight_layout()
                   plt.show()


               case 3:
                   x_column = input("Enter the X column name: ")
                   y_column = input("Enter the Y column name: ")

                   plt.scatter(
                       self.data[x_column],
                       self.data[y_column],
                       color="red"
                   )

                   plt.title(f"{y_column} vs {x_column}")
                   plt.xlabel(x_column)
                   plt.ylabel(y_column)

                   plt.tight_layout()
                   plt.show()
                    
                    
                    
    
h1=SalesDataAnalyzer()
while True:
    print("==========Data Analysis & Visualization Program===================")
    print("please select an option ")
    print("1.Load dataset")
    print("2.Explore Data")
    print("3.Perform DataFrame Operations")
    print("4.Handle missing Data")
    print("5.Generate Descriptive Statistics")
    print("6.Data visualization")
    print("7.Save Visualization ")
    print("8.search and sort and filter")
    print("9.create pivot table ")
    print("Exit")
    
    choice1=int(input("Enter the choice....."))
    match choice1:
        case 1:
            h1.load_data(r"C:/Users/admin/Desktop/python/visualizer/shopify_sales_dataset_ml_eda5.csv")
        case 2:
            h1.explore_data()
        case 3:
            h1.visualize_data()
        case 4:
            h1.clean_data()
        case 5:
            h1.mathematical_operations()
        case 6:
            df2=pd.read_csv(r"C:/Users/admin/Desktop/python/visualizer/shopify_order_details_20_rows.csv")
            print(h1.combine_data(df2))
        case 7:
            h1.aggregate_functions()
        case 8:
            h1.search_sort_filter()
        case 9:
            h1.create_pivot_table()
        
            
            
            
        
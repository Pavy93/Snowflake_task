query_3 = [
    """insert into MASTER_TABLE select id, IOS_App_Id, Title, Developer_Name, Developer_IOS_Id,
       IOS_Store_Url, ifnull(Seller_Official_Website,'-') as Seller_Official_Website, Age_Rating,
       Total_Average_Rating, Total_Number_of_Ratings,
       Average_Rating_For_Version, Number_of_Ratings_For_Version,
       Original_Release_Date, 
       Current_Version_Release_Date, Price_USD,
       Primary_Genre, All_Genres, Languages, Description from STAGE_STREAM
       WHERE METADATA$ACTION = 'INSERT' and
       METADATA$ISUPDATE = False;""",
]

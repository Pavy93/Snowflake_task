query_2 = [
    """insert into STAGE_TABLE select id, IOS_App_Id, Title, Developer_Name, Developer_IOS_Id,
       IOS_Store_Url, Seller_Official_Website, Age_Rating,
       Total_Average_Rating, Total_Number_of_Ratings,
       Average_Rating_For_Version, Number_of_Ratings_For_Version,
       to_timestamp(Original_Release_Date,'YYYY-MM-DD"T"HH24:MI:SS"Z"') as Original_Release_Date, 
       to_timestamp(Current_Version_Release_Date,'YYYY-MM-DD"T"HH24:MI:SS"Z"') as Current_Version_Release_Date,
       Price_USD,
       Primary_Genre, All_Genres, Languages, Description from RAW_STREAM
       WHERE Original_Release_Date <> '0000-00-00T00:00:00Z' and Current_Version_Release_Date <> '0000-00-00T00:00:00Z' 
       and METADATA$ACTION = 'INSERT' and
       METADATA$ISUPDATE = False;""",
]

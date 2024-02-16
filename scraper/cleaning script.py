def Clean_DataFrame(self):
        """
        Allow to convert the data_set list of dict in a DataFrame
        Allow to clean the DataFrame (inner aggregation, conversion, renaming )

        """
        #self.data_set_df = self.Raw_DataFrame()
        self.data_set_df = pd.read_csv('data/raw_data/data_set_RAW_full.csv')
        
        
        
        """to convert the Price in a number format """
        self.data_set_df["Price"] = self.data_set_df["Price"].str.replace(",", "")
        
        
        """ to ensure that numeric to be column are containing numeric data"""
        col_to_conv = [
            "Property ID",
            "Postal code",
            "Open Fire",
            "Price",
            "Construction year",
            "Number of frontages",
            "Covered parking spaces",
            "Outdoor parking spaces",
            "Living area",
            "Bedrooms",
            "Bathrooms",
            "Surface of the plot",
            "Garden surface",
            "Terrace surface",
            "Shower rooms",
        ]
        for col in col_to_conv:
            if col in self.data_set_df.columns:
                self.data_set_df[col] = pd.to_numeric(self.data_set_df[col], downcast='integer')


        """ appartment or house classification creation """
        self.data_set_df["Type of property"] = self.data_set_df[
            "Subtype of property"
        ].apply(
            lambda x: None
            if pd.isnull(x)
            else (
                "Apartment"
                if x
                in [
                    "apartment",
                    "loft",
                    "penthouse",
                    "duplex",
                    "ground-floor",
                    "flat-studio",
                    "service-flat",
                    "kot",
                    "triplex",
                ]
                else "House"
            )
        )


        """ New columns creation (arithmetic or spatial aggregation) """
        self.data_set_df["Parking tot nb"] = (self.data_set_df["Covered parking spaces"].fillna(0) + self.data_set_df["Outdoor parking spaces"].fillna(0))
        self.data_set_df["Bathrooms total nb"] = (self.data_set_df["Bathrooms"].fillna(0) + self.data_set_df["Shower rooms"].fillna(0))

        def province(dfval):
            postal_codes = [range(1000,1300), range(1300, 1500), range(1500,1990), range(3000,3500), range(2000,3000), range(3500,4000), range(4000,5000), range(5000,6000), range(6000,6600), range(7000,8000), range(6600,7000), range(8000,9000), range(9000,10000)]
            provinces = ['Brussels Hoofdstedelijk Gewest', 'Waals-Brabant', 'Vlaams-Brabant', 'Vlaams-Brabant', 'Antwerpen', 'Limburg', 'Luik', 'Namen','Henegouwen', 'Henegouwen','Luxemburg', 'West-Vlaanderen', 'Oost-Vlaanderen']
            for pc_range, prov in zip(postal_codes, provinces):
                if dfval in pc_range:
                    return prov
        self.data_set_df['province'] = self.data_set_df['Postal code'].apply(lambda x: province(x))


        def region(dfval):
            if dfval in range(1300,1500) or dfval in range(4000,7000):
                return 'Wallonia'
            elif dfval in range(1000,1300):
                return 'Brussels'
            else:
                return 'Flanders'
        self.data_set_df['region'] = self.data_set_df['Postal code'].apply(lambda x: region(x))

        """ 
            quali>quanti transformatiion : to create boolean output for all columns where it is possibile 
            through direct converion (yes/no -0/1) or through aggregation 
        """        

        self.data_set_df["New Construction boolean"] = self.data_set_df[
            "Construction year"
        ].apply(lambda x: None if pd.isnull(x) else (0 if x < 2021 else 1))

        self.data_set_df["Tenement building boolean"] = self.data_set_df[
            "Tenement building"
        ].apply(lambda x: None if pd.isnull(x) else (1 if x.lower() == "yes" else 0))

        self.data_set_df["Building condition boolean"] = self.data_set_df[
            "Building condition"
        ].apply(
            lambda x: None
            if pd.isnull(x)
            else (1 if x in ["Asnew", "Good", "Justrenovated"] else 0)
        )

        self.data_set_df["Flood safe boolean"] = self.data_set_df[
            "Flood zone type"
        ].apply(lambda x: None if pd.isnull(x) else (1 if x == "Nonfloodzone" else 0))

        self.data_set_df["Furnished boolean"] = self.data_set_df[
            "Furnished"
        ].apply(lambda x: None if pd.isnull(x) else (1 if x.lower() == "yes" else 0))

      
        self.data_set_df["Kitchen equipped boolean"] = self.data_set_df[
            "Kitchen type"
        ].apply(
            lambda x: None
            if pd.isnull(x)
            else (0 if x in ["Notinstalled", "USAuninstalled"] else 1)
        )

        self.data_set_df["Energy class boolean"] = self.data_set_df[
            "Energy class"
        ].apply(
            lambda x: None
            if pd.isnull(x) or x =='Notspecified'
            else (1 if x in ["A", "A+","A++", "B"] else 0)
        )
        self.data_set_df["Terrace boolean"] = self.data_set_df["Terrace surface"].apply(
            lambda x: 0 if pd.isnull(x) else (1 if x > 0 else 0)
        )

        self.data_set_df["Swimming pool boolean"] = self.data_set_df[
            "Swimming pool"
        ].apply(lambda x: None if pd.isnull(x) else (1 if x.lower() == "yes" else 0))

        self.data_set_df["Garden boolean"] = self.data_set_df["Garden surface"].apply(
            lambda x: 0 if pd.isnull(x) else (1 if x > 0 else 0)
        )
        
        self.data_set_df["Parking boolean"] = self.data_set_df["Parking tot nb"].apply(
            lambda x: None if pd.isnull(x) else (1 if x > 0 else 0)
        )
        
        self.data_set_df["Bathrooms total nb boolean"] = self.data_set_df["Bathrooms total nb"].apply(
            lambda x: None if pd.isnull(x) else (1 if x > 1 else 0)
        )

        self.data_set_df["Elevator boolean"] = self.data_set_df["Elevator"].apply(
            lambda x: None if pd.isnull(x) else (1 if x.lower() == "yes" else 0)
        )

        self.data_set_df["Accessible for disabled people boolean"] = self.data_set_df[
            "Accessible for disabled people"
        ].apply(lambda x: None if pd.isnull(x) else (1 if x.lower() == "yes" else 0))

        self.data_set_df["Double glazing boolean"] = self.data_set_df[
            "Double glazing"
        ].apply(lambda x: None if pd.isnull(x) else (1 if x.lower() == "yes" else 0))


        """ text reformating in a more readable way """

        replace_dict1 = {
            "Asnew": "As new",
            "Justrenovated": "Just renovated",
            "Tobedoneup": "To be done",
            "Torenovate": "To renovate",
            "Torestore" : "To restore"
        }
        replace_dict2 = {
            "Hyperequipped": "Hyper equipped",
            "Semiequipped": "Semi equipped",
            "USAhyperequipped": "USA hyper equipped",
            "Notinstalled": "Not installed",
            "USAinstalled": "USA installed",
            "USAsemiequipped": "USA semi-equipped",
            "USAuninstalled" : "USA uninstalled"
        }
        replace_dict3 = {"Fueloil": "Fuel oil"}

        replace_dict4 = {
            "Nonfloodzone": "Non flood zone",
            "Circumscribedzone": "Circumscribed zone",
            "Possiblecircumscribedwatersidezone": "Possible circumscribed waterside zone",
            "Possiblefloodzone": "Possible flood zone",
            "Recognizedfloodzone": "Recognized flood zone",
            "Propertypartiallyorcompletelylocatedinacircumscribedandrecognizedfloodzone": "Property partially or completely located in a circumscribed and recognized flood zone",
            "Propertypartiallyorcompletelylocatedinacircumscribedfloodzone" : "Property partially or completely located in a circumscribed flood zone",
            "Propertypartiallyorcompletelylocatedinapossiblefloodzoneandlocatedinacircumscribedwatersidezone" : "Property partially or completely located in a possible flood zone and located in a circumscribed waterside zone", 
    }

        replace_dict5 = {"Notspecified": "Not specified"}

        self.data_set_df["Building condition"] = self.data_set_df[
            "Building condition"
        ].replace(replace_dict1)

        self.data_set_df["Kitchen type"] = self.data_set_df["Kitchen type"].replace(
            replace_dict2
        )
        self.data_set_df["Heating type"] = self.data_set_df["Heating type"].replace(
            replace_dict3
        )
        self.data_set_df["Flood zone type"] = self.data_set_df["Flood zone type"].replace(
            replace_dict4
        )
        self.data_set_df["Energy class"] = self.data_set_df["Energy class"].replace(
            replace_dict5
        )
        

        """ column renaming for clarity"""

        self.data_set_df = self.data_set_df.rename(
            columns={
                "url": "URL",
                "Price": "Price (euro)",
                "Surface of the plot": "Plot surface (sqm)",
                "Open Fire": "Open fire",
                "Locality name": "Locality",
                "Subtype of property": "Subtype",
                "Living area": "Living surface (sqm)",
                "Bedrooms": "Nb of Bedrooms",
                "Terrace surface": "Terrace surface (sqm)",
                "Garden surface": "Garden surface (sqm)",
            }
        )
  
        """ Column final Reordering"""

        new_col_order = [
            "Locality",
            "province",
            "region",
            "Postal code",
            "Type of property",
            "Subtype",
            "Price (euro)",
            "Construction year",
            "New Construction boolean",
            "Building condition boolean",
            "Building condition",
            "Energy class boolean",
            "Energy class",
            "Heating type",
            "Double glazing boolean",
            "Double glazing",
            "Elevator boolean",
            "Elevator",
            "Accessible for disabled people boolean",
            "Accessible for disabled people",
            "Living surface (sqm)",
            "Furnished boolean",
            "Furnished",
            "Nb of Bedrooms",
            "Bathrooms total nb boolean",
            "Bathrooms total nb",
            "Bathrooms",
            "Shower rooms",
            "Kitchen equipped boolean",
            "Kitchen type",
            "Open fire",
            "Number of frontages",
            "Swimming pool boolean",
            "Swimming pool",
            "Plot surface (sqm)",
            "Terrace boolean",
            "Terrace surface (sqm)",
            "Garden boolean",
            "Garden surface (sqm)",
            "Parking boolean",
            "Parking tot nb",
            "Covered parking spaces",
            "Outdoor parking spaces",
            "Flood safe boolean",
            "Flood zone type",
            "Tenement building boolean",
            "Tenement building",
            "URL",
            "Property ID",
        ]
        self.data_set_df = self.data_set_df[new_col_order]

        self.data_set_df = self.data_set_df.round(0)

        print(self.data_set_df.head(10))
        print("DataFrame is cleaned!")
        return self.data_set_df 


    def to_csv_clean(self):
        """ 
        Convert the data_set DataFrame into CSV 
        """
        self.data_set_df.to_csv('data/clean_data/data_set_CLEAN.csv', index=False)
        print('A .csv file called "data_set_CLEAN.csv" has been generated. ')
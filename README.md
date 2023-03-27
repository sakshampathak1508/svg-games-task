# svg-games-task

. TO GET THE LIST OF ALL AVAILABLE GAMES AND REQEST AS WELL 
		 		 
		Api Path :- https://web-production-5d0eb.up.railway.app/api/game/
		
    Body for post request:
      eg: in json
        {
        "name": "Clash of clans",
        "url": "https://supercell.com/en/games/clashofclans/",
        "author": "supercell",
        "published_date": "2023-03-22"
      }

      

2. TO GET,PUT,DELETE THE GAME OF ONE PRIMARY KEY ID IS AS FOLLOWS
		
			
		Api Path :- https://web-production-5d0eb.up.railway.app/api/game/
    
    here it is of the type url <int:pk> where you pass the primary key an get put delete address via this url
    
		
		eg: in json for put request
        {
          "id": 1,
          "name": "Clash of for put request plans",
          "url": "https://supercell.com/en/games/clashofclans/",
          "author": "supercell",
          "published_date": "2023-03-22"
        }

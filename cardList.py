
def loadCards():
    cards = {
    ace_hearts : str(""" 
     ---
    |♥  |
    | A |
    |  ♥|
     ---
      
    """) 

    two_hearts : str(""" 
     ---
    |♥  |
    | 2 |
    |  ♥|
     ---
      
    """) 

    three_hearts : str(""" 
     ---
    |♥  |
    | 3 |
    |  ♥|
     ---
      
    """) 

    four_hearts : str(""" 
     ---
    |♥  |
    | 4 |
    |  ♥|
     ---
      
    """) 

    five_hearts : str(""" 
     ---
    |♥  |
    | 5 |
    |  ♥|
     ---
      
    """) 

    six_hearts : str(""" 
     ---
    |♥  |
    | 6 |
    |  ♥|
     ---
      
    """) 

    seven_hearts : str(""" 
     ---
    |♥  |
    | 7 |
    |  ♥|
     ---
      
     """) 

    eight_hearts : str(""" 
     ---
    |♥  |
    | 8 |
    |  ♥|
     ---

    """) 

    nine_hearts : str(""" 
     ---
    |♥  |
    | 9 |
    |  ♥|
     ---
      
    """) 

    ten_hearts : str(""" 
     ---
    |♥  |
    |1 0|
    |  ♥|
     ---
      
     """) 

    jack_hearts : str(""" 
      ---
    |♥  |
    | J |
    |  ♥|
     ---
      
    """) 

    queen_hearts : str(""" 
     ---
    |♥  |
    | Q |
    |  ♥|
     ---

    """) 

    king_hearts : str(""" 
     ---
    |♥  |
    | K |
    |  ♥|
     ---
      
    """) 
     
    ace_diamonds : str(""" 
     ---
    |♦  |
    | A |
    |  ♦|
     ---
      
     """) 

    two_diamonds : str(""" 
     ---
    |♦  |
    | 2 |
    |  ♦|
     ---
      
    """) 

    three_diamonds : str(""" 
     ---
    |♦  |
    | 3 |
    |  ♦|
     ---
      
    """) 

    four_diamonds : str(""" 
     ---
    |♦  |
    | 4 |
    |  ♦|
     ---
      
    """) 

    five_diamonds : str(""" 
     ---
    |♦  |
    | 5 |
    |  ♦|
     ---
      
    """) 

    six_diamonds : str(""" 
     ---
    |♦  |
    | 6 |
    |  ♦|
     ---
      
    """) 

    seven_diamonds : str(""" 
     ---
    |♦  |
    | 7 |
    |  ♦|
    ---
      
        """) 

    eight_diamonds : str(""" 
     ---
    |♦  |
    | 8 |
    |  ♦|
     ---
      
    """) 

    nine_diamonds : str(""" 
     ---
    |♦  |
    | 9 |
    |  ♦|
     ---

     """) 

    ten_diamonds : str(""" 
     ---
    |♦  |
    |1 0|
    |  ♦|
     ---
      
    """) 

    jack_diamonds : str(""" 
     ---
    |♦  |
    | J |
    |  ♦|
     ---
      
    """) 

    queen_diamonds : str(""" 
     ---
    |♦  |
    | Q |
    |  ♦|
     ---

    """) 

    king_diamonds : str(""" 
     ---
    |♦  |
    | K |
    |  ♦|
     ---
      
    """) 

    ace_clubs : str(""" 
     ---
    |♣  |
    | A |
    |  ♣|
     ---
      
    """) 

    two_clubs : str(""" 
     ---
    |♣  |
    | 2 |
    |  ♣|
     ---

    """) 

    three_clubs : str(""" 
     ---
    |♣  |
    | 3 |
    |  ♣|
     ---
      
    """) 

    four_clubs : str(""" 
     ---
    |♣  |
    | 4 |
    |  ♣|
     ---
      
    """) 

    five_clubs : str(""" 
     ---
    |♣  |
    | 5 |
    |  ♣|
     ---
      
    """) 

    six_clubs : str(""" 
     ---
    |♣  |
    | 6 |
    |  ♣|
     ---
      
     """) 

    seven_clubs : str("""
     --- 
    |♣  |
    | 7 |
    |  ♣|
     ---
      
    """) 

    eight_clubs : str(""" 
     ---
    |♣  |
    | 8 |
    |  ♣|
     ---

    """) 

    nine_clubs : str(""" 
     ---
    |♣  |
    | 9 |
    |  ♣|
     ---
      
    """) 

    ten_clubs : str(""" 
     ---
    |♣  |
    |1 0|
    |  ♣|
     ---
      
    """) 

    jack_clubs : str(""" 
     ---
    |♣  |
    | J |
    |  ♣|
     ---
      
    """) 

    queen_clubs : str(""" 
     ---
    |♣  |
    | Q |
    |  ♣|
     ---
      
    """) 

    king_clubs : str(""" 
     ---
    |♣  |
    | K |
    |  ♣|
    ---
      
    """) 
     
    ace_spades : str(""" 
     ---
    |♠  |
    | A |
    |  ♠|
     ---
      
    """) 

    two_spades : str(""" 
     ---
    |♠  |
    | 2 |
    |  ♠|
     ---

    """) 

    three_spades : str(""" 
     ---
    |♠  |
    | 3 |
    |  ♠|
     ---
      
    """) 

    four_spades : str(""" 
     ---
    |♠  |
    | 4 |
    |  ♠|
     ---
      
    """) 

    five_spades : str(""" 
     ---
    |♠  |
    | 5 |
    |  ♠|
     ---
      
    """) 

    six_spades : str(""" 
     ---
    |♠  |
    | 6 |
    |  ♠|
     ---
      
     """) 

    seven_spades : str("""
     --- 
    |♠  |
    | 7 |
    |  ♠|
     ---
      
    """) 

    eight_spades : str(""" 
     ---
    |♠  |
    | 8 |
    |  ♠|
     ---

    """) 

    nine_spades : str(""" 
     ---
    |♠  |
    | 9 |
    |  ♠|
     ---
      
    """) 

    ten_spades : str(""" 
     ---
    |♠  |
    |1 0|
    |  ♠|
     ---
      
    """) 

    jack_spades : str(""" 
     ---
    |♠  |
    | J |
    |  ♠|
     ---
      
    """) 

    queen_spades : str(""" 
     ---
    |♠  |
    | Q |
    |  ♠|
     ---
      
    """) 

    king_spades : str(""" 
     ---
    |♠  |
    | K |
    |  ♠|
    ---
      
    """)
    }

    print("Cards Loaded")

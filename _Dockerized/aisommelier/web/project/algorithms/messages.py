
## Assign specific message to the given quality

def rf_message(rf_predict):

    if rf_predict == 3:
        rf_comment = "Haut Brion that tasted like something that had leaked from a Kleensak."
    elif rf_predict == 4:
        rf_comment = "Medium bodied, light, or classic in style, with its fresh, bright, red berry personality, this is probably going to please some tasters a lot more than others. My quality rating is:"
    elif rf_predict == 5:
        rf_comment = "The wine had great freshness and ample sweetness, but the nose was better than the palate, due to the shortness of the finish. My quality rating is:"
    elif rf_predict == 6:
        rf_comment = "Superb wine, with a complex nose of flowers, coffee bean, licorice, wet earth and plush finish are just now getting to the sweet spot. My quality rating is:"
    elif rf_predict == 7:
        rf_comment = "On the palate, the wine is plush, polished, soft, fresh and loaded with sweet cherries and cassis. My quality rating is:"
    else:
        rf_comment = "Truly outstanding and emotionally thrilling. Full bodied, deep and long, this is drinking in the sweet spot today! My quality rating is:"    
        
    return rf_comment
    
    
def gtb_message(gtb_predict):

    if gtb_predict == 3:
        gtb_comment = "Oh, and what’s the worst wine that I have ever tasted? No need to remember anymore. My quality rating is:"
    elif gtb_predict == 4:
        gtb_comment = "Plain and low quality fruit. On the bright side, it was wet and had alcohol. My quality rating is:"
    elif gtb_predict == 5:
        gtb_comment = "Plush, big, juicy and not shy about its modern style and showy, ripe berries. This a lot of fun to drink today. My quality rating is:"
    elif gtb_predict == 6:
        gtb_comment = "Neo-classic but equally longingly elegant Zinfandel. Drink now through eternity. My quality rating is:"
    elif gtb_predict == 7:
        gtb_comment = "Fleshy, rich, ripe and frankly, lush, this is drinking perfectly today. My quality rating is:"
    else:
        gtb_comment = "Intensity and sexiness. The finish resists fading, serving up dark chocolate and ripe. Truly incomparable! My quality rating is:"    
        
    return gtb_comment
    
    
def vot_message(vot_predict):

    if vot_predict == 3:
        vot_comment = "Only positive is that without bad wine we wouldn’t fully appreciate good wine. My quality rating is:"
    elif vot_predict == 4:
        vot_comment = "Clearly, this is not my style of wine. Much better on the nose than the palate with its smoke, truffle, red berry scented perfume. My quality rating is:"
    elif vot_predict == 5:
        vot_comment = "Good wines, acceptable. But personally I find life too short to waste on boring wines. My quality rating is:"
    elif vot_predict == 6:
        vot_comment = "Unrefined and elegant Cabernet. The wine faded after 20 minutes, but for the initial greeting, it had charm. My quality rating is:"
    elif vot_predict == 7:
        vot_comment = "Medium bodied, finesse styled wine that's fully mature, with freshness in the silky, sweet cherry fruit that really carries through. My quality rating is:"
    else:
        vot_comment = "Balanced, fresh, opulent, long and expansive, this is a contender for the best wine ever to come out of vineyard! My quality rating is:"    
        
    return vot_comment    
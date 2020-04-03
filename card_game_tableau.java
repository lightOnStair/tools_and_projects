import java.util.Random;
final class Card
{

//  RANK NAME. Printable names of card ranks. We don't use index 0.

  private static final String[] rankName =
  {
    "",        //   0
    "ace",     //   1
    "two",     //   2
    "three",   //   3
    "four",    //   4
    "five",    //   5
    "six",     //   6
    "seven",   //   7
    "eight",   //   8
    "nine",    //   9
    "ten",     //  10
    "jack",    //  11
    "queen",   //  12
    "king"     //  13
  };

  private int rank;  //  Card rank, between 1 and 13.

//  CARD. Constructor. Make a new CARD with a given RANK.

  public Card(int rank)
  {
    if (1 <= rank && rank <= 13)
    {
      this.rank = rank;
    }
    else
    {
      throw new IllegalArgumentException("Illegal rank.");
    }
  }

//  GET RANK. Return the RANK of this CARD.

  public int getRank()
  {
    return rank;
  }

//  TO STRING. Return a STRING that describes this CARD, for printing only.

  public String toString()
  {
    return rankName[rank];
  }
}

class Deck
{
  private Card[] deck;
  private int rank = 1;
  private int count = 0;

  public Deck()
  {
    deck = new Card[52];
    for(int i=0;i<52;i+=4)
    {
      deck[i]   = new Card(rank);
      deck[i+1] = new Card(rank);
      deck[i+2] = new Card(rank);
      deck[i+3] = new Card(rank);
      rank++;
    }
  }

  public Card deal()
  {
    Card temp = deck[count];
    count++;
    return temp;
  }

  public void shuffle()
  {
    Random r = new Random();
    if(count>=52)
    {
      throw new IllegalStateException("all cards have been dealt");
    }
    else
    {
      for(int i=deck.length-1;i>0;i--)
      {
        int j = Math.abs(r.nextInt()) % i;
        Card temp = deck[i];
        deck[i] = deck[j];
        deck[j] = temp;
      }
    }
  }
}

class Pile
{
  private class Layer
  {
    private Card card;
    private Layer next;

    private Layer(Card card,Layer layer)
    {
      this.card = card;
      this.next = layer;
    }
  }

  Layer top;

  public Pile()
  {
    top = null;
  }

  public void add(Card card)
  {
    top = new Layer(card,top);
  }

  public Card turn()
  {
    if(isEmpty())
    {
      throw new IllegalStateException("pile is empty");
    }
    else
    {
      Card temp = top.card;
      top = top.next;
      return temp;
    }
  }

  public boolean isEmpty()
  {
    return top == null;
  }


  public Card peek()
  {
    if(isEmpty())
    {
      throw new IllegalStateException("pile is empty");
    }
    else
    {
      return top.card;
    }
  }
}


class Tableau
{
  private Pile[] tableau;
  private Deck deck;

  public Tableau()
  {
    tableau = new Pile[14];
    deck =  new Deck();
    deck.shuffle();
    for(int i=1;i<14;i++)
    {
      tableau[i] = new Pile();
      tableau[i].add(deck.deal());
      tableau[i].add(deck.deal());
      tableau[i].add(deck.deal());
      tableau[i].add(deck.deal());
    }
  }

  public boolean hasWon()
  {
    return (tableau[1].isEmpty() && tableau[2].isEmpty()
          && tableau[3].isEmpty() && tableau[4].isEmpty()
          && tableau[5].isEmpty() && tableau[6].isEmpty()
          && tableau[7].isEmpty() && tableau[8].isEmpty()
          && tableau[9].isEmpty() && tableau[10].isEmpty()
          && tableau[11].isEmpty() && tableau[12].isEmpty()
          && tableau[13].isEmpty());
  }
  public void play()
  {
    int p = 1;
    while(true)
    {
      if(tableau[p].isEmpty())
      {
        if(hasWon())
        {
          System.out.println("You won!");
          return;
        }
        else
        {
          System.out.println("pile " + String.valueOf(p) + " is empty. " + "You lost!");
          return;
        }
      }
      System.out.println("Got " + tableau[p].peek().toString() + " from "+ String.valueOf(p));
      p = tableau[p].turn().getRank();
    }
  }
}

class card_game_tableau
{
  public static void main(String[] args)
  {
    Tableau tableau = new Tableau();
    tableau.play();
  }
}
/*
Here are some game results:

Got eight from 1
Got six from 8
Got two from 6
Got four from 2
Got seven from 4
Got eight from 7
Got five from 8
Got four from 5
Got eight from 4
Got nine from 8
Got two from 9
Got three from 2
Got queen from 3
Got king from 12
Got seven from 13
Got ace from 7
Got seven from 1
Got ten from 7
Got six from 10
Got nine from 6
Got four from 9
Got two from 4
Got six from 2
Got queen from 6
Got ten from 12
Got five from 10
Got three from 5
Got king from 3
Got six from 13
Got king from 6
Got five from 13
Got ten from 5
Got four from 10
Got jack from 4
Got ace from 11
Got ten from 1
Got jack from 10
Got queen from 11
Got eight from 12
Got three from 8
Got king from 3
Got nine from 13
Got queen from 9
Got ace from 12
Got three from 1
Got five from 3
Got nine from 5
Got two from 9
Got jack from 2
Got jack from 11
Got seven from 11
Got ace from 7
You won!


Got eight from 1
Got five from 8
Got six from 5
Got king from 6
Got ten from 13
Got jack from 10
Got king from 11
Got ten from 13
Got two from 10
Got queen from 2
Got three from 12
Got four from 3
Got jack from 4
Got queen from 11
Got six from 12
Got five from 6
Got three from 5
Got four from 3
Got five from 4
Got two from 5
Got six from 2
Got ace from 6
Got three from 1
Got eight from 3
Got seven from 8
Got two from 7
Got nine from 2
Got seven from 9
Got nine from 7
Got queen from 9
Got six from 12
Got king from 6
Got ace from 13
Got nine from 1
Got jack from 9
Got eight from 11
Got seven from 8
Got ten from 7
Got jack from 10
Got five from 11
Got seven from 5
Got king from 7
Got nine from 13
Got ace from 9
Got ten from 1
Got queen from 10
Got four from 12
Got four from 4
Got two from 4
Got three from 2
Got eight from 3
Got ace from 8
You won!

C:\Users\Eric Xie\my pros>java project2_xiexx647
Got six from 2
Got two from 6
Got nine from 2
Got nine from 9
Got queen from 9
Got jack from 12
Got queen from 11
Got ten from 12
Got king from 10
Got five from 13
Got nine from 5
Got eight from 9
Got seven from 8
Got four from 7
Got ten from 4
Got ace from 10
Got two from 1
Got nine from 2
Got queen from 9
Got four from 12
Got five from 4
Got two from 5
Got jack from 2
Got king from 11
Got ten from 13
Got queen from 10
Got ace from 12
Got six from 1
Got jack from 6
Got three from 11
Got three from 3
Got seven from 3
Got king from 7
Got five from 13
Got two from 5
pile 2 is empty. You lost!

C:\Users\Eric Xie\my pros>java project2_xiexx647
Got jack from 2
Got ten from 11
Got six from 10
Got eight from 6
Got eight from 8
Got two from 8
Got four from 2
Got nine from 4
Got five from 9
Got ten from 5
Got jack from 10
Got six from 11
Got four from 6
Got two from 4
Got jack from 2
Got king from 11
Got queen from 13
Got ace from 12
Got two from 1
Got three from 2
Got ten from 3
Got king from 10
Got king from 13
Got seven from 13
Got six from 7
Got queen from 6
Got ace from 12
Got four from 1
Got queen from 4
Got five from 12
Got jack from 5
Got nine from 11
Got eight from 9
Got seven from 8
Got three from 7
Got seven from 3
Got six from 7
Got eight from 6
Got ace from 8
Got ace from 1
Got two from 1
pile 2 is empty. You lost!
*/

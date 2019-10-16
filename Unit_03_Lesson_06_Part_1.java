//Omar Naeem
//Unit 03 Lesson 06 Part 1
//1/27/2018

import java.util.Scanner;

public class Unit_03_Lesson_06_Part_1
{
	String word;
	char letter;
	int guesses = 8;
	String s;
	int index;
	int wordLength;

	public String enterWord()
	{
		Scanner input = new Scanner(System.in);
		System.out.println("[Player 1] Enter the word/phrase (in lowercase) to be guessed: ");
		word = input.nextLine();
		System.out.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");

		wordLength = word.length();
		s = word.replaceAll("[*a-z]","-");
		System.out.println("The dashes below signify letters of the word/phrase. Spaces in the dashes signify actual spaces in the word/phrase.");
		return s;
	}
	public void guessingWord()
	{
		Scanner input = new Scanner(System.in);
		System.out.println("[Player 2] You have a total of 8 guesses to determine the word/phrase.");

		while(guesses > 0 && !s.equals(word))
		{
			System.out.println("[Player 2] Enter a letter: ");
			letter = input.next().charAt(0);

			if(word.indexOf(letter) >= 0)
			{
				System.out.println("Correct!");

				index = word.indexOf(letter);
				while(index >= 0)
				{
					s = s.substring(0,index) + letter + s.substring(index + 1);
					index = word.indexOf(letter, index + 1);
				}
				System.out.println(s);

				if(s.equals(word))
				{
					System.out.println("Congratulations, you guessed the phrase/word: " + word);
					break;
				}
			}
			else
			{
				guesses--;
				System.out.println("Incorrect");
				System.out.println("Guesses remaining: " + guesses);

				if(guesses == 0)
				{
					System.out.println("Game Over! You Lost! The actual word was: " +  word);
				}
			}
		}

	}
	public static void main(String args[])
	{
		Scanner input = new Scanner(System.in);
		Unit_03_Lesson_06_Part_1 x = new Unit_03_Lesson_06_Part_1();
		System.out.println(x.enterWord());
		x.guessingWord();
	}

}
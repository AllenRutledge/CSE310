package module01;

import java.util.Scanner;
import java.util.Random;

class Hangman {
    static Scanner input;

    public static void hangman() {
        input = new Scanner(System.in);
        // A list of 120 strings.
        String[] words = { "ABOUT", "ABOVE", "ACROSS", "AFTER", "AGAIN", "ALMOST", "ALSO", "AROUND", "BACK", "BACKED",
                "BEFORE", "BELOW", "BETWEEN", "BOTH", "CALL", "COME", "COULD", "EACH", "EVEN", "EVENT", "FIND", "FIRST",
                "FIVE", "FOUR", "FROM", "GOTTEN", "APPLE", "BEACH", "BRAIN", "BREAD", "BRUSH", "CHAIR", "CHEST",
                "CHORD", "CLICK", "CLOCK", "CLOUD", "DANCE", "DIARY", "DRINK", "EARTH", "FLUTE", "FRUIT", "GHOST",
                "GRAPE", "GREEN", "HAPPY", "HEART", "HOUSE", "JUICE", "LIGHT", "MONEY", "MUSIC", "PARTY", "PIZZA",
                "PLANT", "RADIO", "RIVER", "SALAD", "SHEEP", "SHARD", "SMILE", "SNACK", "SNAKE", "SPICE", "SPOON",
                "STORM", "TABLE", "TOAST", "TOASTING", "TIGER", "TRAIN", "WATER", "WHALE", "WHEEL", "WOMAN", "WORLD",
                "WRITE", "YOUTH", "GIVE", "GREAT", "GREATER", "GREATEST", "HALF", "HALVES", "MISS", "WRONG", "HAVE",
                "HERE", "HERS", "INTO", "JUST", "KNOW", "LIKE", "LONG", "LOOK", "MADE", "MANY", "MORE", "MOST", "ONLY",
                "OTHER", "OUR", "OUTER", "OVER", "PEOPLE", "SAID", "SAME", "SEEING", "SOME", "TAKE", "TELL", "THAN",
                "THAT", "THEIR", "THEM", "THEN", "THERE", "THESE", "THEY", "THIS", "THREE", "VERY", "VIOLIN",
                "VIOLENCE", "WELL", "WHAT", "WHEN", "WHERE", "WHICH", "WILL", "WITH", "WORK", "WORKS", "YOUR",
                "YOURS" };
        // Tells the player the game has started.
        System.out.println("Hangman has started! Selecting word...");
        Random thing = new Random();
        // Pick one of the 120 words. It doesn't seem to start at 0.
        int rng = thing.nextInt(120);
        String secretWord = (words[rng]);

        // Censor word, and start game.
        String wordBlank = secretWord.replaceAll("[A-Z]", "_ ");
        System.out.println("Word selected!");
        start(secretWord, wordBlank);
    }

    public static void start(String secretWord, String wordBlank) {
        // Tries, times got wrong, a guess, a letter, whether or not the guess has
        // already been attempted, the list of guesses, and whether or not the guess was
        // correct.
        int wrong = 0;
        String guess;
        char letter;
        boolean triedGuess;
        String guesses = "";
        boolean goodGuess;
        while (wrong < 7 && wordBlank.contains("_")) {
            // While the misses are under 7, and blank spaces are present, tell the player
            // how many tries are left.
            System.out.println((7 - wrong) + " TRIES REMAINING");
            // Show the word with the blank spaces and await the player's letter input. Only
            // the first letter is read if you decide to break the rules and put in more
            // than one letter.
            System.out.println(wordBlank);
            System.out.println("Guess: ");
            guess = input.nextLine();
            guess = guess.toUpperCase();
            letter = guess.charAt(0);
            // triedGuess activates when the player uses a letter already present in the
            // string of guesses.
            triedGuess = (guesses.indexOf(letter)) != -1;
            guesses += letter;
            // Uppercases player input to disable case sensitivity.
            letter = Character.toUpperCase(letter);

            goodGuess = (secretWord.indexOf(letter)) != -1;
            if (goodGuess == true) {
                // If the letter is present, swap the correct letter with the blanks where they
                // belong.
                System.out.println("CORRECT!");
                for (int position = 0; position < secretWord.length(); position++) {
                    if (secretWord.charAt(position) == letter && wordBlank.charAt(position) != letter) {
                        wordBlank = wordBlank.replaceAll("_ ", "_");
                        String wordBuffer = wordBlank.substring(0, position) + letter
                                + wordBlank.substring(position + 1);
                        wordBuffer = wordBuffer.replaceAll("_", "_ ");
                        wordBlank = wordBuffer;
                    }
                }
            } else {
                // Count something as wrong, unless the incorrect letter was already guessed.
                if (triedGuess == true) {
                    System.out.println("THAT WAS ALREADY GUESSED!");
                    continue;
                }
                System.out.println(letter + " NOT PRESENT");
                wrong++;
            }
        }
        if (wrong == 7) {
            // Clear console, then show game over screen.
            System.out.print("\033\143");
            System.out.println("  []===[-]    ");
            System.out.println("  ||    |     ");
            System.out.println("  ||    O     ");
            System.out.println("  ||   /|\\    ");
            System.out.println("  ||    |     ");
            System.out.println("  ||   / \\    ");
            System.out.println("  ||          ");
            System.out.println(" _[]_________ ");
            System.out.println("|____________|");
            System.out.println("GAME OVER, THE WORD WAS " + secretWord + "!");
        } else {
            // Clear console, then show victory screen alongside the number of misses.
            System.out.print("\033\143");
            System.out.println("  []===[-]    ");
            System.out.println("  ||          ");
            System.out.println("  ||          ");
            System.out.println("  ||          ");
            System.out.println("  ||   \\O/    ");
            System.out.println("  ||    |     ");
            System.out.println("  ||    |     ");
            System.out.println(" _[]___/_\\___ ");
            System.out.println("|____________|");
            System.out.println("YOU GOT '" + secretWord + "' IN " + wrong + " TRIES! YOU WIN!");
        }
    }

    public static void main(String[] args) {
        hangman();
    }
}
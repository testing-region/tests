import java.util.Scanner;

/**
 * This program implements the "Stones Game". In this game, two players take
 * turns picking stones from an initial pile of stones (the starting number of
 * stones must be odd), until there are no stones left.
 * The player who ends up with an odd number of stones wins.
 *
 * @author David Saah
 * @version 1.0
 * @since 2023-01-27
 *
 */
public class App {
    public static void main(String[] args) {
        // Initialise StonesGame object to handle game data.
        StonesGame stonesGame = new StonesGame();

        // Initialise Scanner object to get input from the user.
        Scanner getInput = new Scanner(System.in);

        // Get total stones from user.
        System.out.print("How many stones do you want to use?: ");
        int totalStones = getInput.nextInt();

        /*
         * Checks if the stone number is an odd positive number,
         * else ask the user for a valid input.
         */
        while (true) {
            if (totalStones > 0 && totalStones % 2 != 0) {
                stonesGame.setTotalStones(totalStones);
                break;
            } else {
                System.out.println("\nThe number of stones must be an odd positive number!");
                System.out.print("How many stones do you want to use?: ");
                totalStones = getInput.nextInt();
            }
        }

        // create a new line to make output readable.
        System.out.println();

        /*
         * Call nextLine method for Scanner object to absorb the newline character
         * left by nextInt method called above.
         */
        getInput.nextLine();

        /*
         * Get the usernames of players.
         * Initialise player objects with the chosen username.
         */
        System.out.print("Player 1 username: ");
        Player player1 = new Player(getInput.nextLine());
        System.out.print("Player 2 username: ");
        Player player2 = new Player(getInput.nextLine());

        /*
         * Set the limit on the number of stones the first player can pick when the game
         * starts. This is half the total number of stones.
         */
        int limit = (int) stonesGame.getTotalStones() / 2;

        stonesGame.setStonesLimit(limit);
        int playerStoneChoice = 0;

        /*
         * Start the main game loop.
         * Keep loop running until the total stones is 0.
         */
        while (stonesGame.getTotalStones() > 0) {
            /*
             * Get the summary of the players
             * Display game summary
             */
            System.out.println();
            player1.getInfo();
            player2.getInfo();
            stonesGame.getInfo();

            /*
             * Keep prompting player 1 to pick the valid number of stones.
             * Valid number of stones are positive and less than the stone selection limit.
             */
            do {
                stonesGame.promt(player1.getName());
                playerStoneChoice = getInput.nextInt();
            } while ((playerStoneChoice <= 0) || (playerStoneChoice > stonesGame.getStonesLimit()));

            // Update player 1 stones and total stones count.
            player1.updateStonesCount(playerStoneChoice);
            stonesGame.updateTotalStones(playerStoneChoice);

            /*
             * Stone selection limit boundary is defined by:
             * - the current number of stones.
             * - 2 times the number of stones picked by the previous player.
             *
             * The stone selection limit is the smaller boundary value.
             * Update the stone selection limit.
             */
            if (stonesGame.getTotalStones() < (2 * playerStoneChoice)) {
                stonesGame.setStonesLimit(stonesGame.getTotalStones());
            } else {
                stonesGame.setStonesLimit(2 * playerStoneChoice);
            }

            /*
             * Player 1 may potentially pick all stones left in the pile.
             * Break the main game loop if the total stones get finished.
             */
            if (stonesGame.getTotalStones() == 0) {
                break;
            }

            /*
             * Get the summary of the players
             * Display game summary
             */
            System.out.println();
            player1.getInfo();
            player2.getInfo();
            stonesGame.getInfo();

            /*
             * Keep prompting player 2 to pick the valid number of stones.
             * Valid number of stones are positive and less than the stone selection limit.
             */
            do {
                stonesGame.promt(player2.getName());
                playerStoneChoice = getInput.nextInt();
            } while ((playerStoneChoice <= 0) || (playerStoneChoice > stonesGame.getStonesLimit()));

            // Update player 2 stones and total stones count.
            player2.updateStonesCount(playerStoneChoice);
            stonesGame.updateTotalStones(playerStoneChoice);

            /*
             * Update the stone selection limit.
             * Picks the lower value of the two boundaries for player stone selection limit.
             */
            if (stonesGame.getTotalStones() < (2 * playerStoneChoice)) {
                stonesGame.setStonesLimit(stonesGame.getTotalStones());
            } else {
                stonesGame.setStonesLimit(2 * playerStoneChoice);
            }

        }

        System.out.println();
        System.out.println("Game Over: There are no more stones left!");

        /**
         * The player with the odd number of stones win.
         * Determine the player with the odd number of stones.
         * Display a congratulatory message for the winner.
         *
         */
        if (player1.getStonesCount() % 2 != 0) {
            System.out.printf("Congratulations %s, you won the game.\n", player1.getName());
        } else {
            System.out.printf("Congratulations %s, you won the game.\n", player2.getName());
        }

        // Close the scanner to prevent a memory leak.
        getInput.close();
    }
}

/**
 * This class handles the implementation of the "Stones Game".
 * Functions:
 * - Updates and keeps track of the total stone count.
 * - Updates and keeps track of the stone selection limit.
 * - Handles prompt message for selecting stones.
 *
 */
class StonesGame {
    private int totalStones;
    private int stonesLimit;

    /**
     * Sets the total number of stones chosen.
     *
     * @param totalStones the total number of stones chosen for the game.
     *
     */
    public void setTotalStones(int totalStones) {
        this.totalStones = totalStones;
    }

    /**
     * Gets the current total number of stones.
     *
     * @return the number of stones left to choose from.
     *
     */
    public int getTotalStones() {
        return totalStones;
    }

    /**
     * Updates the total number of stones.
     *
     * @param stonesNum the number of stones a player chooses.
     *
     */
    public void updateTotalStones(int stonesNum) {
        this.totalStones -= stonesNum;
    }

    /**
     * Sets the limit for the number of stones a player can choose.
     *
     * @param stonesLimit the stone number threshold a player cannot exceed.
     *
     */
    public void setStonesLimit(int stonesLimit) {
        this.stonesLimit = stonesLimit;
    }

    /**
     * Gets the stone number selection limit.
     *
     * @return the stone number threshold a player cannot exceed.
     *
     */
    public int getStonesLimit() {
        return stonesLimit;
    }

    /**
     * Displays a message that tells the number of stones left in the pile.
     *
     */
    public void getInfo() {
        System.out.printf("There are %d stones left in the pile.\n", totalStones);
    }

    /**
     * Displays a message prompt that tells the stone number range a player can
     * choose from.
     *
     * @param playerName the name of the current player's turn.
     *
     */
    public void promt(String playerName) {
        if (!(stonesLimit == 1)) {
            System.out.printf("\n%s, choose between 1 and %d: ", playerName, stonesLimit);
        } else {
            System.out.printf("\n%s, There is 1 stone left: ", playerName);
        }
    }
}

/**
 * This class handles the attributes and actions of a player.
 *
 */
class Player {
    private String name;
    private int playerStoneCount;

    /**
     * Player constructor.
     * Initialises the name and the stone count a player has.
     *
     * @param name player's name
     *
     */
    public Player(String name) {
        this.name = name;
        this.playerStoneCount = 0;
    }

    /**
     * Gets the name of the player.
     *
     * @return the player's name.
     *
     */
    public String getName() {
        return name;
    }

    /**
     * Gets the number of stones a player has.
     *
     * @return the number of stones a player has.
     *
     */
    public int getStonesCount() {
        return playerStoneCount;
    }

    /**
     * Updates the number of stones a player has.
     *
     * @param stonesNum the number of stones a player chooses.
     *
     */
    public void updateStonesCount(int stonesNum) {
        this.playerStoneCount += stonesNum;
    }

    /**
     * Displays the number of stones a player possesses.
     *
     */
    public void getInfo() {
        System.out.printf("%s has %d stones.\n", name, playerStoneCount);
    }

}

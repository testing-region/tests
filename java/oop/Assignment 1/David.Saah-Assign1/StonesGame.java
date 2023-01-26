import java.util.Scanner;

public class StonesGame {
	public static void main(String[] args) {
		Scanner getInput = new Scanner(System.in);
		System.out.print("How many stones do you want to use?: ");
		int totalStones = getInput.nextInt();

		while (true) {
			if (totalStones > 0 && totalStones % 2 != 0) {
				break;
			} else {
				System.out.println("\nThe number of stones must be an odd positive number!");
				System.out.print("How many stones do you want to use?: ");
				totalStones = getInput.nextInt();
			}
		}

		System.out.println();
		getInput.nextLine();

		System.out.print("Player 1 username: ");
		Player player1 = new Player(getInput.nextLine());

		System.out.print("Player 2 username: ");
		Player player2 = new Player(getInput.nextLine());

		int player1Stones = 0, player2Stones = 0;
		int stoneLimit = (int) (totalStones / 2);

		while (totalStones > 0) {
			System.out.printf("\n%s has %d stones.\n", player1, player1Stones);
			System.out.printf("%s has %d stones.\n", player2, player2Stones);
			System.out.printf("There are %d stones left in the pile.\n", totalStones);
			System.out.printf("\n%s, choose between 1 and %d: ", player1, stoneLimit);
			int playerStoneChoice = getInput.nextInt();

			if ((playerStoneChoice > 0) && (playerStoneChoice <= stoneLimit)) {
				player1Stones += playerStoneChoice;
				totalStones -= playerStoneChoice;
				stoneLimit = totalStones < (2 * playerStoneChoice) ? totalStones : 2 * playerStoneChoice;
			} else if (playerStoneChoice <= 0) {
				System.out.println("\n[!] You must pick at least one stone.");
				continue;
			} else {
				System.out.println("\n[!] You cannot pick a stone above the limit.");
				continue;
			}

			if (totalStones != 0) {
				System.out.printf("\n%s has %d stones.\n", player1, player1Stones);
				System.out.printf("%s has %d stones.\n", player2, player2Stones);
				System.out.printf("There are %d stones left in the pile.\n", totalStones);
				System.out.printf("\n%s, choose between 1 and %d: ", player2, stoneLimit);
				playerStoneChoice = getInput.nextInt();
			} else {
				break;
			}

			if ((playerStoneChoice > 0) && (playerStoneChoice <= stoneLimit)) {
				player2Stones += playerStoneChoice;
				totalStones -= playerStoneChoice;
				stoneLimit = totalStones < (2 * playerStoneChoice) ? totalStones : 2 * playerStoneChoice;
			} else if (playerStoneChoice <= 0) {
				System.out.println("\n[!] You must pick at least one stone.");
				continue;
			} else {
				System.out.println("\n[!] You cannot pick a stone above the limit.");
				continue;
			}

		}

		String winner;

		if (player1Stones % 2 != 0) {
			winner = player1;
		} else {
			winner = player2;
		}

		System.out.println();
		System.out.println("Game Over: There are no more stones left.");
		System.out.printf("Congratulations %s, you won the game.\n", winner);
		getInput.close();
	}
}

class Player {
	private String name;
	private int playerStoneCount;

	public Player(String name) {
		this.name = name;
		this.playerStoneCount = 0;
	}

	public String getName() {
		return name;
	}

	public int getStonesCount() {
		return playerStoneCount;
	}

	public void setStonesCount(int stonesNum) {
		this.playerStoneCount = stonesNum;
	}

}
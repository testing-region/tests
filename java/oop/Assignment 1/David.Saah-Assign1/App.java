import java.util.Scanner;

public class App {
	public static void main(String[] args) {
		StonesGame stonesGame = new StonesGame();

		Scanner getInput = new Scanner(System.in);
		System.out.print("How many stones do you want to use?: ");
		int totalStones = getInput.nextInt();

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

		System.out.println();
		getInput.nextLine();

		System.out.print("Player 1 username: ");
		Player player1 = new Player(getInput.nextLine());
		System.out.print("Player 2 username: ");
		Player player2 = new Player(getInput.nextLine());

		int limit = (int) stonesGame.getTotalStones() / 2;

		stonesGame.setStonesLimit(limit);
		int playerStoneChoice = 0;

		while (stonesGame.getTotalStones() > 0) {
			System.out.println();
			player1.getInfo();
			player2.getInfo();
			stonesGame.getInfo();

			do {
				stonesGame.promt(player1.getName());
				playerStoneChoice = getInput.nextInt();
			} while ((playerStoneChoice <= 0) || (playerStoneChoice > stonesGame.getStonesLimit()));

			player1.updateStonesCount(playerStoneChoice);
			stonesGame.updateTotalStones(playerStoneChoice);

			if (stonesGame.getTotalStones() < (2 * playerStoneChoice)) {
				stonesGame.setStonesLimit(stonesGame.getTotalStones());
			} else {
				stonesGame.setStonesLimit(2 * playerStoneChoice);
			}

			if (stonesGame.getTotalStones() == 0) {
				break;
			}

			System.out.println();
			player1.getInfo();
			player2.getInfo();
			stonesGame.getInfo();

			do {
				stonesGame.promt(player2.getName());
				playerStoneChoice = getInput.nextInt();
			} while ((playerStoneChoice <= 0) || (playerStoneChoice > stonesGame.getStonesLimit()));

			player2.updateStonesCount(playerStoneChoice);
			stonesGame.updateTotalStones(playerStoneChoice);

			if (stonesGame.getTotalStones() < (2 * playerStoneChoice)) {
				stonesGame.setStonesLimit(stonesGame.getTotalStones());
			} else {
				stonesGame.setStonesLimit(2 * playerStoneChoice);
			}

		}

		System.out.println();
		System.out.println("Game Over: There are no more stones left.");

		if (player1.getStonesCount() % 2 != 0){
			System.out.printf("Congratulations %s, you won the game.\n", player1.getName());
		} else {
			System.out.printf("Congratulations %s, you won the game.\n", player2.getName());
		}

		getInput.close();
	}
}

class StonesGame {
	private int totalStones;
	private int stonesLimit;

	public void setTotalStones(int totalStones) {
		this.totalStones = totalStones;
	}

	public int getTotalStones() {
		return totalStones;
	}

	public void updateTotalStones(int stonesNum) {
		this.totalStones -= stonesNum;
	}

	public void setStonesLimit(int stonesLimit) {
		this.stonesLimit = stonesLimit;
	}

	public int getStonesLimit() {
		return stonesLimit;
	}

	public void getInfo() {
		System.out.printf("There are %d stones left in the pile.\n", totalStones);
	}

	public void promt(String playerName) {
		if (!(stonesLimit == 1)) {
			System.out.printf("\n%s, choose between 1 and %d: ", playerName, stonesLimit);
		} else {
			System.out.printf("\n%s, There is 1 stone left: ", playerName);
		}
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

	public void updateStonesCount(int stonesNum) {
		this.playerStoneCount += stonesNum;
	}

	public void getInfo() {
		System.out.printf("%s has %d stones.\n", name, playerStoneCount);
	}

}
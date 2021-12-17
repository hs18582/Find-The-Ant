import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.layout.Pane;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class Minesweeper extends Application {

    private int TILE_SIZE = 50;
    private static final int W = 800;
    private static final int H = 600;

    private int X_TILES = W / TILE_SIZE;
    private int Y_TILES = H / TILE_SIZE;
    private final String[] gameType = {"Easy", "Medium", "Hard", "Very Hard"};
    private String difficulty;

    @FXML
    private Menu gameMenu;

    private Tile[][] grid = new Tile[X_TILES][Y_TILES];
    private Scene scene;

    public MenuBar menu() {
        gameMenu = new Menu("Difficulty");
        for(String game : gameType){
            MenuItem menuItem = new MenuItem(game);
            menuItem.setUserData(game);
            menuItem.setOnAction((ActionEvent event) -> {
                selectGame(event);
            });
            gameMenu.getItems().add(menuItem);
        }
        MenuBar menuBar = new MenuBar(gameMenu);
        return menuBar;
    }

    private void selectGame(ActionEvent event) {
        MenuItem menuItem = (MenuItem)event.getSource();
        difficulty = (String)menuItem.getUserData();
        switch (difficulty) {
            case "Easy":
                TILE_SIZE = 200;
                break;
            case "Medium":
                TILE_SIZE = 100;
                break;
            case "Hard":
                TILE_SIZE = 50;
                break;
            case "Very Hard":
                TILE_SIZE = 40;
                break;
            default:
                break;
        }
    }

    private Parent createContent() {
        VBox root = new VBox();
        Pane content  = new Pane();
        content.setPrefSize(W, H);

        for (int y = 0; y < Y_TILES; y++) {
            for (int x = 0; x < X_TILES; x++) {
                Tile tile = new Tile(x, y, Math.random() < 0.1);

                grid[x][y] = tile;
                content .getChildren().add(tile);
            }
        }

        for (int y = 0; y < Y_TILES; y++) {
            for (int x = 0; x < X_TILES; x++) {
                Tile tile = grid[x][y];

                if (tile.antFound)
                    continue;

                long bombs = getNeighbors(tile).stream().filter(t ->      t.antFound).count();

                if (bombs > 0)
                    tile.text.setText(String.valueOf(bombs));
            }
        }
        root.getChildren().addAll(menu(),content);
        return root;
    }

    private List<Tile> getNeighbors(Tile tile) {
        List<Tile> neighbors = new ArrayList<>();

        int[] points = new int[] {
                -1, -1,
                -1, 0,
                -1, 1,
                0, -1,
                0, 1,
                1, -1,
                1, 0,
                1, 1
        };

        for (int i = 0; i < points.length; i++) {
            int dx = points[i];
            int dy = points[++i];

            int newX = tile.x + dx;
            int newY = tile.y + dy;

            if (newX >= 0 && newX < X_TILES
                    && newY >= 0 && newY < Y_TILES) {
                neighbors.add(grid[newX][newY]);
            }
        }

        return neighbors;
    }

    private class Tile extends StackPane {
        private int x, y;
        private boolean antFound;
        private boolean isOpen = false;

        private Rectangle border = new Rectangle(TILE_SIZE - 2, TILE_SIZE - 2);
        private Text text = new Text();

        Alert alert = new Alert(AlertType.CONFIRMATION, "Game Over! Play   Again?");

        public Tile(int x, int y, boolean hasBomb) {
            this.x = x;
            this.y = y;
            this.antFound = hasBomb;

            border.setStroke(Color.LIGHTGRAY);

            text.setFont(Font.font(18));
            text.setText(hasBomb ? "X" : "");
            text.setVisible(false);

            getChildren().addAll(border, text);

            setTranslateX(x * TILE_SIZE);
            setTranslateY(y * TILE_SIZE);

            setOnMouseClicked(e -> open());
        }

        public void open() {
            if (isOpen)
                return;

            if (antFound) {
                Optional<ButtonType> result = alert.showAndWait();
                if (result.isPresent() && result.get() == ButtonType.OK) {
                    scene.setRoot(createContent());
                }
                return;
            }

            isOpen = true;
            text.setVisible(true);
            border.setFill(null);

            if (text.getText().isEmpty()) {
                getNeighbors(this).forEach(Tile::open);
            }

            switch (text.getText()) {
                case "1":
                    text.setFill(Color.BLUE);
                    break;
                case "2":
                    text.setFill(Color.FORESTGREEN);
                    break;
                case "3":
                    text.setFill(Color.RED);
                    break;
                case "4":
                    text.setFill(Color.DARKBLUE);
                    break;
                case "5":
                    text.setFill(Color.MAROON);
                    break;
                case "6":
                    text.setFill(Color.AQUAMARINE);
                    break;
                case "7":
                    text.setFill(Color.BLACK);
                    break;
                case "8":
                    text.setFill(Color.GRAY);
                    break;
                default:
                    break;
            }
        }
    }

    @Override
    public void start(Stage stage) throws Exception {
        scene = new Scene(createContent());

        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
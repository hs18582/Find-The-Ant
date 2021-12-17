package FindTheAnt;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.stage.Stage;

import java.io.IOException;


public class FindTheAnt extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        Window window = new Window(600,600,"Find The Ant",stage);
        window.openWindow();
        stage.setOnCloseRequest(event -> {
            Platform.exit();
            System.exit(0);
        });
    }

    public static void main(String[] args) {
        launch();
    }
}
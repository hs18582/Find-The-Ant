package FindTheAnt;

import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.util.Duration;

import java.util.Timer;
import java.util.TimerTask;


public class AntGame {
    Scene scene;
    Window window;
    GameCanvas gCanvas;
    private static final int FRAME_RATE = 20;
    private static final int FRAMES_BEFORE_RESET = FRAME_RATE * 30;
    int frameReset;
    Timeline timeline;


    public AntGame(Window window){
        //Rectangle2D primaryScreenBounds = Screen.getPrimary().getBounds();
        this.window = window;
        Pane pane = new Pane();
        scene = new Scene(pane);
        window.stage.setScene(scene);
        window.stage.setWidth(625);
        window.stage.setHeight(625);
        gCanvas = new GameCanvas (600, 600);
        pane.getChildren().add(gCanvas.canvas);

        start();

    }

    public void start() {
        Timer t = new Timer();
        t.schedule(new TimerTask() {
            @Override
            public void run() {
                setEventHandlers();
            }
        }, 1000);

        startUpdateDrawLoop();
    }


    private void  startUpdateDrawLoop() {
        timeline = new Timeline(new KeyFrame(
                Duration.millis(1000.0/FRAME_RATE),
                actionEvent -> {
                    update();
                    draw();
                }
        ));
        timeline.setCycleCount(Timeline.INDEFINITE);
        timeline.play();
    }

    public void stop() {
        timeline.stop();
    }




    public void update() {
        if (frameReset <= 0){
            frameReset = FRAMES_BEFORE_RESET;
        }
        frameReset--;
    }

    public void draw(){
        gCanvas.draw();
    }

    private void setEventHandlers() {
        scene.setOnKeyPressed(event -> stop());
        // Commented the code out so that we don't have to be careful about touching the mouse
        scene.setOnMouseMoved(event -> stop());
        scene.setOnMouseClicked(event -> stop());
    }

}

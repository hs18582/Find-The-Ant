package main.java;
import javafx.scene.control.Button;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;

public class dunno {
    public void addButtons(Pane parentPane) {
        HBox[] hb = new HBox[9];
        Button[][] btn = new Button[9][9];
        // A for loop in another for loop to create 2d button arrays.

        for (int i = 0; i < hb.length; i++) {
            hb[i] = new HBox();
            for (int j = 0; j < btn.length; j++) {
                btn[i][j] = new CustomButton(i, j);

                hb[i].getChildren().add(btn[i][j]);
            }

            parentPane.getChildren().add(hb[i]);
        }
    }

    class CustomButton extends Button {
        private int i;
        private int j;

        public CustomButton(int i, int j) {
            super();
            this.i = i;
            this.j = j;

            setText(i + "/" + j);

            setOnAction(event -> {
                System.out.println(getI() + " " + getJ());
            });
        }

        public int getI() {
            return i;
        }

        public int getJ() {
            return j;
        }
    }
}

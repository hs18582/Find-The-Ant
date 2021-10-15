import javax.swing.JFrame;

public class Ant extends JFrame{

    public Ant() {
        add(new Model());
    }


    public static void main(String[] args) {
        Ant ant = new Ant();
        ant.setVisible(true);
        ant.setTitle("Find the Ant");
        ant.setSize(380,420);
        ant.setDefaultCloseOperation(EXIT_ON_CLOSE);
        ant.setLocationRelativeTo(null);

    }

}
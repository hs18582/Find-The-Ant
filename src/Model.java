import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.Timer;

public class Model extends JPanel implements ActionListener {

    private Dimension d;
    private boolean inGame = false;
    private final int BLOCK_SIZE = 24;
    private final int N_BLOCKS = 15;
    private Image up, down, left, right;
    private int Ant_x, Ant_y, Antd_x, Antd_y;
    private int req_dx, req_dy;
    private int currentSpeed = 3;
    private short[] screenData;
    private Timer timer;

    public Model() {

        loadImages();
        initVariables();
        addKeyListener(new TAdapter());
        setFocusable(true);
    }


    private void loadImages() {
        down = new ImageIcon("C:\\Users\\hs18582\\IdeaProjects\\snake\\src\\antdown.png").getImage();
        up = new ImageIcon("C:\\Users\\hs18582\\IdeaProjects\\snake\\src\\/antup.png").getImage();
        left = new ImageIcon("C:\\Users\\hs18582\\IdeaProjects\\snake\\src\\antleft.png").getImage();
        right = new ImageIcon("C:\\Users\\hs18582\\IdeaProjects\\snake\\src\\antright.png").getImage();
    }
    private void initVariables() {

        screenData = new short[N_BLOCKS * N_BLOCKS];
        d = new Dimension(400, 400);

        timer = new Timer(40, this);
        timer.start();
    }

    private void playGame(Graphics2D g2d) {

            moveAnt();
            drawAnt(g2d);
            checkMaze();

    }

    private void showIntroScreen(Graphics2D g2d) {

        String start = "Press SPACE to start";
        g2d.setColor(Color.yellow);
        int SCREEN_SIZE = N_BLOCKS * BLOCK_SIZE;
        g2d.drawString(start, (SCREEN_SIZE)/4, 150);
    }

    private void checkMaze() {

        int i = 0;
        boolean finished = true;

        while (i < N_BLOCKS * N_BLOCKS && finished) {

            if ((screenData[i]) != 0) {
                finished = false;
            }

            i++;
        }

        if (finished) {

            int maxSpeed = 6;
            if (currentSpeed < maxSpeed) {
                currentSpeed++;
            }

        }
    }

    private void moveAnt() {

        int pos;
        short ch;

        if (Ant_x % BLOCK_SIZE == 0 && Ant_y % BLOCK_SIZE == 0) {
            pos = Ant_x / BLOCK_SIZE + N_BLOCKS * (Ant_y / BLOCK_SIZE);
            ch = screenData[pos];

            if ((ch & 16) != 0) {
                screenData[pos] = (short) (ch & 15);
                //score++;
            }

            if (req_dx != 0 || req_dy != 0) {
                if (!((req_dx == -1 && req_dy == 0 && (ch & 1) != 0)
                        || (req_dx == 1 && req_dy == 0 && (ch & 4) != 0)
                        || (req_dx == 0 && req_dy == -1 && (ch & 2) != 0)
                        || (req_dx == 0 && req_dy == 1 && (ch & 8) != 0))) {
                    Antd_x = req_dx;
                    Antd_y = req_dy;
                }
            }

            // Check for standstill
            if ((Antd_x == -1 && Antd_y == 0 && (ch & 1) != 0)
                    || (Antd_x == 1 && Antd_y == 0 && (ch & 4) != 0)
                    || (Antd_x == 0 && Antd_y == -1 && (ch & 2) != 0)
                    || (Antd_x == 0 && Antd_y == 1 && (ch & 8) != 0)) {
                Antd_x = 0;
                Antd_y = 0;
            }
        }
        int Ant_SPEED = 6;
        Ant_x = Ant_x + Ant_SPEED * Antd_x;
        Ant_y = Ant_y + Ant_SPEED * Antd_y;
    }

    private void drawAnt(Graphics2D g2d) {

        if (req_dx == -1) {
            g2d.drawImage(left, Ant_x + 1, Ant_y + 1, this);
        } else if (req_dx == 1) {
            g2d.drawImage(right, Ant_x + 1, Ant_y + 1, this);
        } else if (req_dy == -1) {
            g2d.drawImage(up, Ant_x + 1, Ant_y + 1, this);
        } else {
            g2d.drawImage(down, Ant_x + 1, Ant_y + 1, this);
        }
    }


    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        Graphics2D g2d = (Graphics2D) g;

        g2d.setColor(Color.red);
        g2d.fillRect(0, 0, d.width, d.height);

        if (inGame) {
            playGame(g2d);
        } else {
            showIntroScreen(g2d);
        }

        Toolkit.getDefaultToolkit().sync();
        g2d.dispose();
    }


    //controls
    class TAdapter extends KeyAdapter {

        @Override
        public void keyPressed(KeyEvent e) {

            int key = e.getKeyCode();

            if (inGame) {
                if (key == KeyEvent.VK_LEFT) {
                    req_dx = -1;
                    req_dy = 0;
                } else if (key == KeyEvent.VK_RIGHT) {
                    req_dx = 1;
                    req_dy = 0;
                } else if (key == KeyEvent.VK_UP) {
                    req_dx = 0;
                    req_dy = -1;
                } else if (key == KeyEvent.VK_DOWN) {
                    req_dx = 0;
                    req_dy = 1;
                } else if (key == KeyEvent.VK_ESCAPE) {
                    inGame = false;
                }
            } else {
                if (key == KeyEvent.VK_SPACE) {
                    inGame = true;
                }
            }
        }
    }


    @Override
    public void actionPerformed(ActionEvent e) {
        repaint();
    }

}
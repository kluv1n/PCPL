public class Bisquare {
    private double coefA;
    private double coefB;
    private double coefC;
    private int kolRoots;
    private double[] roots;

    // Конструктор
    public Bisquare() {
        this.coefA = 0.0;
        this.coefB = 0.0;
        this.coefC = 0.0;
        this.kolRoots = 0;
        this.roots = new double[0]; // Инициализация пустого массива
    }

    // Геттеры и сеттеры
    public double getCoefA() {
        return coefA;
    }

    public void setCoefA(double coefA) {
        this.coefA = coefA;
    }

    public double getCoefB() {
        return coefB;
    }

    public void setCoefB(double coefB) {
        this.coefB = coefB;
    }

    public double getCoefC() {
        return coefC;
    }

    public void setCoefC(double coefC) {
        this.coefC = coefC;
    }

    public int getKolRoots() {
        return kolRoots;
    }

    public void setKolRoots(int kolRoots) {
        this.kolRoots = kolRoots;
    }

    public double[] getRoots() {
        return roots;
    }

    public void setRoots(double[] roots) {
        this.roots = roots;
    }

    // Ввод коэффициентов с консоли или командной строки
    public double inputCoef(String[] args, int index, String text) {
        Scanner scanner = new Scanner(System.in);
        String coefStr = "";

        try {
            coefStr = args[index];
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println(text);
            coefStr = scanner.nextLine();
        }

        return Double.parseDouble(coefStr);
    }

    public void getCoef(String[] args) {
        this.setCoefA(inputCoef(args, 0, "Введите A:"));
        this.setCoefB(inputCoef(args, 1, "Введите B:"));
        this.setCoefC(inputCoef(args, 2, "Введите C:"));
    }

    // Решение уравнения
    public void solution() {
        double a = this.getCoefA();
        double b = this.getCoefB();
        double c = this.getCoefC();
        double d = b * b - 4 * a * c; // Дискриминант

        if (d < 0.0) {
            this.setKolRoots(0);
        } else if (d == 0.0) {
            double t = (-b + Math.sqrt(d)) / (2 * a);
            if (t < 0.0) {
                this.setKolRoots(0);
            } else if (t == 0.0) {
                this.setRoots(new double[1]);
                this.getRoots()[0] = t;
                this.setKolRoots(1);
            } else {
                this.setRoots(new double[2]);
                this.getRoots()[0] = Math.sqrt(t);
                this.getRoots()[1] = -Math.sqrt(t);
                this.setKolRoots(2);
            }
        } else {
            double t1 = (-b + Math.sqrt(d)) / (2 * a);
            double t2 = (-b - Math.sqrt(d)) / (2 * a);
            if (t1 < 0.0) {
                if (t2 < 0.0) {
                    this.setKolRoots(0);
                } else if (t2 == 0.0) {
                    this.setRoots(new double[1]);
                    this.getRoots()[0] = 0;
                    this.setKolRoots(1);
                } else {
                    this.setRoots(new double[2]);
                    this.getRoots()[0] = Math.sqrt(t2);
                    this.getRoots()[1] = -Math.sqrt(t2);
                    this.setKolRoots(2);
                }
            } else if (t1 == 0.0) {
                if (t2 < 0.0) {
                    this.setRoots(new double[1]);
                    this.getRoots()[0] = 0;
                    this.setKolRoots(1);
                } else if (t2 == 0.0) {
                    this.setRoots(new double[1]);
                    this.getRoots()[0] = 0;
                    this.setKolRoots(1);
                } else {
                    this.setRoots(new double[3]);
                    this.getRoots()[0] = 0;
                    this.getRoots()[1] = Math.sqrt(t2);
                    this.getRoots()[2] = -Math.sqrt(t2);
                    this.setKolRoots(3);
                }
            } else {
                if (t2 < 0.0) {
                    this.setRoots(new double[2]);
                    this.getRoots()[0] = Math.sqrt(t1);
                    this.getRoots()[1] = -Math.sqrt(t1);
                    this.setKolRoots(2);
                } else if (t2 == 0.0) {
                    this.setRoots(new double[3]);
                    this.getRoots()[0] = Math.sqrt(t1);
                    this.getRoots()[1] = -Math.sqrt(t1);
                    this.getRoots()[2] = 0;
                    this.setKolRoots(3);
                } else {
                    this.setRoots(new double[4]);
                    this.getRoots()[0] = Math.sqrt(t1);
                    this.getRoots()[1] = -Math.sqrt(t1);
                    this.getRoots()[2] = Math.sqrt(t2);
                    this.getRoots()[3] = -Math.sqrt(t2);
                    this.setKolRoots(4);
                }
            }
        }
    }

    // Печать корней
    public void printRoots() {
        if (this.getKolRoots() != this.getRoots().length) {
            System.out.println(String.format("Ошибка. Уравнение содержит %d действительных корней, но было вычислено %d корней.",
                    this.getKolRoots(), this.getRoots().length));
        } else {
            switch (this.getKolRoots()) {
                case 0:
                    System.out.println("Нет корней");
                    break;
                case 1:
                    System.out.println("Один корень: " + this.getRoots()[0]);
                    break;
                case 2:
                    System.out.println(String.format("Два корня: %f и %f", this.getRoots()[0], this.getRoots()[1]));
                    break;
                case 3:
                    System.out.println(String.format("

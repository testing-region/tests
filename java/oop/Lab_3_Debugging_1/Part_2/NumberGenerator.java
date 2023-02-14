package Part_2;

import java.util.Iterator;

/**
 * "NumberGenerator is an Iterable that generates a sequence of numbers."
 *
 *
 */
public class NumberGenerator implements Iterable<Integer> {

    private int start;

    private int stop;

    private int step;

    /**
     * @param start
     * @param stop
     * @param step
     */
    // A constructor.
    public NumberGenerator(int start, int stop, int step) {
        this.start = start;
        this.stop = stop;
        this.step = step;
    }

    public NumberGenerator(int start, int stop) {
        this.start = start;
        this.stop = stop;
        this.step = 1;
    }

    public NumberGenerator(int stop) {
        this.start = 0;
        this.stop = stop;
        this.step = 1;
    }

    @Override
    public Iterator<Integer> iterator() {
        // TODO Auto-generated method stub
        return new NumberGeneratorIterator(this);
    }

    /**
     * @return the start
     */
    public int getStart() {
        return start;
    }

    /**
     * @return the stop
     */
    public int getStop() {
        return stop;
    }

    /**
     * @return the step
     */
    public int getStep() {
        return step;
    }

}

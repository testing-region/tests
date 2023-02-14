package Part_2;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class NumberGeneratorIterator implements Iterator<Integer> {

    private NumberGenerator _generator;

    private Integer marker;

    private int _bug_marker = 6;
    private int count = 0;

    public NumberGeneratorIterator(NumberGenerator generator) {
        this._generator = generator;
        this.marker = _generator.getStart() - _generator.getStep();

    }

    @Override
    public boolean hasNext() {
        return this._generator.getStep() <= 0 ? this.marker + this._generator.getStep() > this._generator.getStop()
                : this.marker + this._generator.getStep() < this._generator.getStop();
    }

    @Override
    public Integer next() {
        if (this.hasNext()) {
            this.marker += this._generator.getStep();
            this.count++;
            return this.marker + (this._bug_marker == this.count ? 1 : 0);
        }
        throw new NoSuchElementException();
    }

}

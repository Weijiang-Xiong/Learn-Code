import { useState } from "react";

const Display = ({ counter }) => {
    return <div>{counter}</div>;
};

const Button = ({ onClick, label }) => {
    return <button onClick={onClick}>{label}</button>;
}

const App = () => {
    const [counter, setCounter] = useState(0);

    const addOne = () => setCounter(counter + 1);
    const subOne = () => setCounter(counter - 1);
    const reset = () => setCounter(0);

    return (
        <div>
            <Display counter={counter} />
            <Button onClick={addOne} label="Add One" />
            <Button onClick={subOne} label="Subtract One" />
            <Button onClick={reset} label="Reset" />
        </div>
    );
};

export default App;

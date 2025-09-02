import { useState } from "react";
import './App.css';

const StatContents = (props) => {
    if (props.total === 0) {
        return <div className="no-stats">the app is used by pressing the buttons</div>;
    }
    return (
        <div className="stats-container">
            <table>
                <tbody>
                    <tr>
                        <td>Good:</td>
                        <td>{props.good}</td>
                    </tr>
                    <tr>
                        <td>Neutral:</td>
                        <td>{props.neutral}</td>
                    </tr>
                    <tr>
                        <td>Bad:</td>
                        <td>{props.bad}</td>
                    </tr>
                    <tr>
                        <td>Total:</td>
                        <td>{props.total}</td>
                    </tr>
                    <tr>
                        <td>Average:</td>
                        <td>{props.average.toFixed(2)}</td>
                    </tr>
                    <tr>
                        <td>Positive Feedback:</td>
                        <td>{props.positive.toFixed(2)}%</td>
                    </tr>
                </tbody>
            </table>
        </div>
    )
};

const Button = ({ onClick, text }) => {
    const getDataType = () => {
        if (text === 'Good') return 'good';
        if (text === 'Neutral') return 'neutral';
        if (text === 'Bad') return 'bad';
        return '';
    };
    return <button data-type={getDataType()} onClick={onClick}>{text}</button>;
};

const App = () => {
    const [good, setGood] = useState(0);
    const [neutral, setNeutral] = useState(0);
    const [bad, setBad] = useState(0);

    const getTotal = () => {
        return good + neutral + bad;
    };

    const getPositivePercentage = () => {
        const total = getTotal();
        return total === 0 ? 0 : (good / total) * 100;
    };
    const getAverage = () => {
        const total = getTotal();
        return total === 0 ? 0 : (good - bad) / total;
    };

    return (
        <div className="app-container">
            <h3>Give Feedback</h3>
            <div className="feedback-buttons">
                <Button onClick={() => setGood(good + 1)} text="Good" />
                <Button onClick={() => setNeutral(neutral + 1)} text="Neutral" />
                <Button onClick={() => setBad(bad + 1)} text="Bad" />
            </div>
            <h3>Statistics</h3>
            <StatContents
                good={good}
                neutral={neutral}
                bad={bad}
                total={getTotal()}
                average={getAverage()}
                positive={getPositivePercentage()}
            />
        </div>
    );
};

export default App;

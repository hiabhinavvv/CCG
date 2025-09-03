import "react"
import { useState, useEffect } from "react"
import {MCQChallenge} from "./MCQChallenge.jsx"
import {useApi} from "../utils/api.js"

export function ChallengeGenerator() {
    const [challenge, setChallenge] = useState(null)
    const [isloading, setIsLoading] = useState(false)
    const [error, setError] = useState(null)
    const [difficulty, setDifficulty] = useState("easy")
    const [quota, setQuota] = useState(null)
    const {makeRequest} = useApi()
    const [topic, setTopic] = useState("topic1")


    useEffect(() => {
        fetchQuota()
    }, [])    

    const fetchQuota = async () => {
        try {
            const data = await makeRequest("quota")
            setQuota(data)
        } catch (err) {
            console.log(err)
        }
    }

    const generateChallenge = async () => {
        setIsLoading(true)
        setError(null)

        try {
            const data = await makeRequest("generate-challenge", {
                method: 'POST',
                body: JSON.stringify({difficulty, topic})
                }
            )
            setChallenge(data)
            fetchQuota()
        } catch (err) {
            setError(err.message || 'failed to generate challenge')
        } finally {
            setIsLoading(false)
        }   
    }

    const getNextResetTime = () => {
        if (!quota?.last_reset_data) return null
        const resetDate = new Date(quota.last_reset_data)
        resetDate.setHours(resetDate.getHours()+24)
        return resetDate
    }
    
    return <div className="challenge-container">
        <h2>QUIZ</h2>

        <div className="quota-display">
            <p>Quota Remaining Today: {quota?.quota_remaining || 0}</p>
            {quota?.quota_remaining === 0 && (
                <p>Next Reset: {getNextResetTime()?.toLocaleString()}</p>
            )}
        </div>

        <div className="difficulty-selector">
            <label htmlFor="topic">
                Select Topic:
            </label>
            <select id="topic"
                value={topic}
                onChange={(e) => setTopic(e.target.value)}
                disabled={isloading}>
                <option value="topic1">Machine Learning Fundamentals</option>
                <option value="topic2">Neural Networks and Deep Learning</option>
                <option value="topic3">Computer Vision</option>
                <option value="topic4">Natural Language Processing</option>
                <option value="topic5">Reinforcement Learning</option>
                <option value="topic6">Data Structures and Algorithms</option>
                <option value="topic7">AI Ethics</option>
            </select>
        </div>

        <div className="difficulty-selector">
            <label htmlFor="difficulty">
                Select Difficulty:
            </label>
            <select id="difficulty"
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value)}
            disabled = {isloading}>
                <option value="easy">Easy</option>
                <option value="medium">Medium</option>
                <option value="hard">Hard</option>
            </select>
        </div>

        <button className="generate-button"
            onClick={generateChallenge}
            disabled={false}
        >
            {isloading ? "Generating...." : "Get Question"}
        </button>

        {error && <div className="error-message">
            <p>{error}</p>
        </div>}

        {challenge && <MCQChallenge challenge={challenge}/>}


    </div>
}
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
                body: JSON.stringify({difficulty})
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
        <h2>coding challenge generator</h2>

        <div className="quota-display">
            <p>challenge remaining today: {quota?.quota_remaining || 0}</p>
            {quota?.quota_remaining === 0 && (
                <p>next reset: {getNextResetTime()?.toLocaleString()}</p>
            )}
        </div>

        <div className="difficulty-selector">
            <label htmlFor="difficulty">
                select difficulty:
            </label>
            <select id="difficulty"
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value)}
            disabled = {isloading}>
                <option value="easy">easy</option>
                <option value="medium">medium</option>
                <option value="hard">hard</option>
            </select>
        </div>

        <button className="generate-button"
            onClick={generateChallenge}
            disabled={false}
        >
            {isloading ? "generating...." : "generate challenge"}
        </button>

        {error && <div className="error-message">
            <p>{error}</p>
        </div>}

        {challenge && <MCQChallenge challenge={challenge}/>}


    </div>
}
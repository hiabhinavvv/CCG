import "react"
import {SignIn, SignUp, SignedIn, SignedOut} from "@clerk/clerk-react"

export function AuthenticationPage() {
    return (
        <div className="auth-page">
            <div className="auth-wrapper">
                <SignedOut>
                    <div className="auth-card">
                        <div className="auth-header">
                            <div className="logo">
                                <div className="logo-icon">
                                    <span>▲</span>
                                </div>
                                <h1 className="brand-name">ALGOPREP</h1>
                            </div>
                        </div>
                        
                        <div className="auth-content">
                            <SignIn routing="path" path='/sign-in'/>
                            <SignUp routing="path" path='/sign-up'/>
                        </div>
                        
                        <div className="auth-footer">
                            <p>© ALGOPREP 2025</p>
                            <p>Powered By Clerk Authentication</p>
                        </div>
                    </div>
                </SignedOut>
                
                <SignedIn>
                    <div className="redirect-message">
                        <p>You are already signed in.</p>
                    </div>
                </SignedIn>
            </div>
        </div>
    )
}

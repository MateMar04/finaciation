import React, {useContext, useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import AuthContext from "../context/AuthContext";
import getAdvised from "../services/AdviseeServices";

const AdvisedPage = () => {

    const {id} = useParams()

    let advisedId = id
    let [advised, setAdvised] = useState(null)
    let {authTokens, logoutUser} = useContext(AuthContext)

    useEffect(() => {
        getAdvised(authTokens.access).then(data => setAdvised(data))
    }, [advisedId])

    return (
        <div>
            <h1>{advised?.first_name} {advised?.last_name}</h1>
        </div>
    )
}

export default AdvisedPage;
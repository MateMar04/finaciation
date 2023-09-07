import '../assets/styles/RowWithCheck.css'
import { Button, Col, Modal, Row } from "react-bootstrap";
import { Form } from "react-bootstrap";
import React, { useContext, useState, useEffect } from "react";
import AuthContext from "../context/AuthContext";
import TextField from '@mui/material/TextField';
import InputAdornment from '@mui/material/InputAdornment';
import AccountCircleOutlinedIcon from '@mui/icons-material/AccountCircleOutlined';
import { Container, Card } from 'react-bootstrap';
import '../assets/styles/AddMayorPage.css';
import FailedModal from "../components/FailedModal";
import SucceedModal from "../components/SucceedModal";
import {getMayors } from '../services/MayorServices';

export const MayorModifyModal = (mayor, props) => {

    let { authTokens } = useContext(AuthContext)
    const [showfail, setShowfailture] = useState(false);
    const [showsuccess, setShowsuccese] = useState(false);
    const toggleModalsucceed = () => setShowsuccese(!showsuccess);
    const toggleModalfailed = () => setShowfailture(!showfail);
    let [mayors, setMayors] = useState([])

    useEffect(() => {
        getMayors(authTokens.access).then(data => setMayors(data))
    }, [])

    let postMayor = async (e) => {
        e.preventDefault();

        const firstName = e.target.first_name.value;
        const lastName = e.target.last_name.value;

        // Check if either the first name or last name is empty
        if (!firstName || !lastName) {
            // Display an error message or take appropriate action
            toggleModalfailed();
            return;
        }

        let response = await fetch('/api/mayors', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                "Authorization": "JWT " + String(authTokens.access),
                "Accept": "application/json"
            },
            body: JSON.stringify({
                "first_name": firstName,
                "last_name": lastName
            })
        });

        if (response.status === 200) {
            toggleModalsucceed();
        } else if (response.status === 500) {
            toggleModalfailed();
        } else if (response.status === 401) {
            toggleModalfailed();
        } else if (response.status === 400) {
            toggleModalfailed();
        }
    }

    return (
        <Modal show={props.show} >
            <SucceedModal onClose={() => toggleModalsucceed()} message="la visita" show={showsuccess} />
            <FailedModal onClose={() => toggleModalfailed()} message="la visita" show={showfail} />
            <Container className="containermayor container-addmayor-modal">

                <Form onSubmit={postMayor}>
                    <h3 className={'h3LoginPage'}>Seleccione Intendente</h3>

                    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                        <select className='select' id="standard-basic" variant="standard" >
                            <option selected disabled hidden></option>
                            {mayors?.map((mayor) => (
                                <option value={mayor.id}>{mayor.first_name} {mayor.last_name}</option>
                            ))}
                        </select>
                        <p>
                            <a>
                                Nombre: {mayor.first_name}
                            </a>
                            <a>
                                Apellido: {mayor.last_name}
                            </a>
                        </p>
                    </div>


                    <div style={{ textAlign: 'center', marginTop: '20px' }}>
                        <Button className='BtnIniciarSesionLogin' type="submit">Registrar</Button>
                    </div>
                    <div style={{ textAlign: 'center', marginTop: '10px' }}>
                        <Button variant="outlined" color="primary" onClick={props.onClose}>
                            Cancelar
                        </Button>
                    </div>
                </Form>
            </Container>
        </Modal>


    )
}

export default MayorModifyModal
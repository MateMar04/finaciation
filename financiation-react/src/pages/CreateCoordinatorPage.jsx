import React, {useContext, useState} from "react";
import {Button, Container, Form} from "react-bootstrap";
import '../assets/styles/ActivateAccountPAge.css'
import AuthContext from "../context/AuthContext";
import {SucceedModal} from "../components/SucceedModal"
import FailedModal from "../components/FailedModal";

const CoordinatorPage = () => {
    let {authTokens} = useContext(AuthContext)
    const [showfail, setShowfailture] = useState(false);
    const [showsuccess, setShowsuccese] = useState(false);
    const toggleModalsucceed = () => setShowsuccese(!showsuccess);
    const toggleModalfailed = () => setShowfailture(!showfail);


    let postCoordinator = async (e) => {
        e.preventDefault()
        let response = await fetch('/api/coordinators', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                "Authorization": "JWT " + String(authTokens.access),
                "Accept": "application/json"
            },
            body: JSON.stringify({
                "id_user": e.target.id_user.value,
                "id_group": e.target.id_group.value
            })
        })
        if (response.status === 200) {
            toggleModalsucceed();
            await postCoordinator()
        } else if (response.status == 500) {
            toggleModalfailed();
            //alert('no se a registrado la visita (Uno de los datos ingresados no coincide con la base de datos)')
            await postCoordinator()
        } else if (response.status == 401) {
            toggleModalfailed();
            //alert('no se a registrado la visita (Desautorizado)')
            await postCoordinator()
        } else if (response.status == 400) {
            toggleModalfailed();
            //alert('no se a registrado la visita (Bad request)')
            await postCoordinator()
        }
    }


    return (
        <Container className="scrolling">
            <SucceedModal message="el coordinador" show={showsuccess}/>
            <FailedModal message="el coordinador" show={showfail}/>
            <Form onSubmit={postCoordinator}>
                <Form.Group>
                    <Form.Control
                        type="number"
                        placeholder="Enter user id"
                        name="id_user"
                        required
                    />
                </Form.Group>
                <Form.Group>
                    <Form.Control
                        type="number"
                        placeholder="Enter group id"
                        name="id_group"
                        required
                    />
                </Form.Group>
                <Form.Group>
                    <Button type="submit">Submit</Button>
                </Form.Group>
            </Form>

        </Container>
    );
}

export default CoordinatorPage;
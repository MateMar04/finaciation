import { Col, Container, Row } from "react-bootstrap";
import "../assets/styles/MainMenuPage.css";
import Card from "@mui/material/Card";
import Avatar from "@mui/material/Avatar";
import React, { useContext, useEffect, useState } from "react";
import AuthContext from "../context/AuthContext";
import VisitCardMainMenu from "../components/VisitCardMainMenu";
import BarChart from "../components/BarChart";
import VerMasButton from "../components/VerMasButton";
import { Link } from "react-router-dom";
import { getLatestVisitRequests, getLatestVisits } from "../services/VisitServices";
import { getUserGroup } from "../services/GroupServices";
import { PersonRowMainMenu } from "../components/PersonRowMainMenu";
import { getMyUser, getUser, getUserById } from "../services/UserServices";
import { getUserStatusesById } from "../services/StatusServices";
import { getUserRolesById } from "../services/RoleServices";
import { Zoom } from "@mui/material";



export const MainMenuPage = () => {

    let { authTokens, user } = useContext(AuthContext)
    const [myUser, setMyUser] = useState()
    const [latestVisits, setLatestVisits] = useState()
    const [latestVisitRequests, setLatestVisitRequests] = useState()
    const [userGroup, setUserGroup] = useState([])
    let [role, setRole] = useState([])
    let [status, setStatus] = useState([])
    const [lastReqLoc, setLastReqLoc] = useState()


    const getData = async () => {
        const usuario = await getUser(authTokens.access)
        setMyUser(usuario)
        getLatestVisits(authTokens.access).then(r => setLatestVisits(r))
        getLatestVisitRequests(authTokens.access).then(r => setLatestVisitRequests(r))
        getUserGroup(authTokens.access, usuario.id).then(r => setUserGroup(r))
        getUserStatusesById(authTokens.access, usuario.user_status).then(data => setStatus(data))
        getUserRolesById(authTokens.access, usuario.role).then(data => setRole(data))
    }

    useEffect(() => {

        getData();

    }, []);

    useEffect(() => {
        if (latestVisitRequests && latestVisitRequests.length > 0) {
            setLastReqLoc(latestVisitRequests[0].location)
        }

    }, [latestVisitRequests]);

    return (
        <Container fluid className="main-menu-container">
            <Row>
                <Col lg={4}>
                    <Zoom in style={{ transitionDelay: '100ms' }}>
                        <Card className="profile-card " id="left-card">
                            

                            <Container className={'d-flex align-items-center'}>
                                <Container>

                                    <Row>
                                        <Col className="d-flex justify-content-center">
                                            <Avatar src={'data:image/png;base64, ' + myUser?.profile_picture}
                                                sx={{ width: 128, height: 128 }} />
                                        </Col>
                                    </Row>

                                    <Row className="text-center">
                                        <strong>
                                            <h3>{myUser?.first_name} {myUser?.last_name}</h3>
                                        </strong>
                                    </Row>

                                    <Container>
                                        <Row>
                                            <strong>
                                                <p className="p-main-menu-card">Estado:</p>
                                            </strong>
                                        </Row>
                                        <Row>
                                            <Col xs={1} md={3}>
                                                <p className="p-main-menu-card">{status?.name}</p>
                                            </Col>
                                            <Col xs={1} md={1} className="justify-content-end">
                                                {status.name === 'Disponible' && (
                                                    <a className="circle_green text-center"></a>
                                                )}
                                                {status.name === 'Ocupado' && (
                                                    <a className="circle_red text-center"></a>
                                                )}

                                            </Col>
                                        </Row>
                                        <Row>
                                            <strong>
                                                <p className="p-main-menu-card">Rol:</p>
                                            </strong>
                                        </Row>
                                        <Row>
                                            <p className="p-main-menu-card">{role?.name}</p>
                                        </Row>
                                        <Row>
                                            <strong>
                                                <p className="p-main-menu-card">Cuil:</p>
                                            </strong>
                                        </Row>
                                        <p className="p-main-menu-card">{myUser?.ssn}</p>
                                    </Container>
                                </Container>
                            </Container>
                            <Row className={'justify-content-end'}>
                                <Col md={4} xs={6}>
                                    <Link to={'/me'}>
                                        <VerMasButton />
                                    </Link>
                                </Col>
                            </Row>

                        </Card></Zoom>
                    <Zoom in style={{ transitionDelay: '150ms' }}>
                        <Card className="last-visits-card border d-flex align-items-center" id="left-card">
                            <Container className="">
                                <Row className="text-center first-row-main-menu-card">
                                    <h4>Consultas resueltas en la ultima visita en {lastReqLoc}:</h4>
                                </Row>
                                <Row className="text-center">
                                    {latestVisitRequests && latestVisitRequests.length > 0 ? (
                                        <h3 className="fw-bold">{latestVisitRequests[0].requests}</h3>
                                    ) : (
                                        <p>No visit requests available</p>
                                    )}
                                </Row>
                            </Container>
                        </Card>
                    </Zoom>
                </Col>

                <Col lg={4}>
                    <Zoom in style={{ transitionDelay: '200ms' }}>
                        <Card className="next-visits-card" id="center-card">
                            <Container>
                                <Row className="text-center">
                                    <h2 className="name-title">Próximas Visitas</h2>
                                </Row>
                                <Container className="container-visit-card-main-menu">
                                    {latestVisits?.map((visit) => (
                                        <VisitCardMainMenu name={visit.name} status={visit.status} />
                                    ))}
                                </Container>
                                <Link to={'/visits'}>
                                    <Row className={'justify-content-end'}>
                                        <Col md={4} xs={6}>
                                            <VerMasButton className={'ver-mas-bottom-visit'} />
                                        </Col>
                                    </Row>
                                </Link>

                            </Container>
                        </Card>
                    </Zoom>
                </Col>

                <Col lg={4}>
                    <Zoom in style={{ transitionDelay: '250ms' }}>
                        <Card className="group-card-main-menu" id="right-card">
                            
                            <Row className="text-center justify-content-center">
                                {userGroup && userGroup.length > 0 ? (
                                    <h2 className="name-title">{userGroup[0].group}</h2>
                                ) : (
                                    <h2 className="name-title" onClick={() => console.log(userGroup)}>Sin Grupo</h2>
                                )}

                            </Row>
                            <Row id="nombresscroll" className="text-center justify-content-center ">

                                {userGroup?.map((i) => (
                                    <PersonRowMainMenu role={i?.role} first_name={i?.first_name} last_name={i?.last_name} />
                                ))}
                            </Row>
                            <Row className={'justify-content-end'}>
                                <Col md={4} xs={6}>
                                    <Link to={'/groups'}>
                                        <VerMasButton />
                                    </Link>
                                </Col>
                            </Row>
                        </Card>
                    </Zoom>
                    <Zoom in style={{ transitionDelay: '300ms' }}>
                        <Card className="report-card-main-menu d-flex align-items-center" id="right-card">
                            <Container>
                                <Row className="text-center">
                                    <h2 className="name-title ">Consultas</h2>
                                </Row>
                                <Row>

                                    <BarChart className="barchart-report-card-main-menu" chartData={{
                                        labels: ["Pedro", "Maria", "Juan"],
                                        datasets: [{
                                            label: "",
                                            data: [30, 30, 40],
                                            backgroundColor: ["red", "green", "blue"]
                                        }]
                                    }} />

                                </Row>
                            </Container>
                        </Card>
                    </Zoom>
                </Col>
            </Row>
        </Container>
    )
}
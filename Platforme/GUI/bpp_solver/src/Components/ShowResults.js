import React from "react";
import Container from "@material-ui/core/Container";
import { withStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CardHeader from "@material-ui/core/CardHeader";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";

class ShowResults extends React.Component {
  constructor(props) {
    super(props);
    this.retourClick = this.retourClick.bind(this);
    this.ecart_show = this.ecart_show.bind(this);
    this.state = {
      ecart: -1,
    };
  }

  retourClick() {
    this.props.handleretour();
  }
  ecart_show(ecart, classes) {
    let ecart_field = "";
    console.log(ecart);
    if (this.props.ecart) {
      ecart_field = (
        <TextField
          className={classes.textfield}
          id="filled-read-only-input"
          label="Ecart"
          defaultValue={ecart+"%"}
          InputProps={{
            readOnly: true,
          }}
          variant="filled"
        />
      );
    }
    return ecart_field;
  }
  render() {
    const { solutions, classes } = this.props;

    return (
      <Container className={classes.root}>
        <div className={classes.emptyheight}></div>
        <Typography variant="h4" className={classes.pagetitle} gutterBottom>
          Résultats
        </Typography>
        {solutions.map(({ key, label, texec, nb, ecart, boites }) => {
          return (
            <div>
              <div>{""}</div>
              <Card key={key}>
                <CardContent>
                  <CardHeader textsize="5" title={label} />
                  <TextField
                    className={classes.textfield}
                    id="filled-read-only-input"
                    label="Nombre de boîtes utilisées"
                    defaultValue={nb}
                    InputProps={{
                      readOnly: true,
                    }}
                    variant="filled"
                  />
                  <TextField
                    className={classes.textfield}
                    id="filled-read-only-input"
                    label="Temps d'execution"
                    defaultValue={texec}
                    InputProps={{
                      readOnly: true,
                    }}
                    variant="filled"
                  />
                  {this.ecart_show(ecart, classes)}
                  <div className={classes.listSol}>
                    <label className={classes.text_contenu}>
                      Contenu des boîtes
                    </label>
                    <List component="nav">
                      {boites.map(({ idbin, objects }) => {
                        let objs = "[ ";
                        objects.forEach(
                          (item) => (objs = objs + item.poid + ", ")
                        );
                        objs = objs + "]";
                        return (
                          // get the liste "objects" of idbin so that
                          <ListItem button key={idbin}>
                            <ListItemText
                              className={classes.text_contenu_b}
                              primary={"Boîte " + idbin + ": " + objs}
                            />
                          </ListItem>
                        );
                      })}
                    </List>
                  </div>
                </CardContent>
              </Card>
              <div className={classes.emptyheight} />
            </div>
          );
        })}
        <Button
          className={classes.btn}
          onClick={this.retourClick}
          variant="contained"
          size="large"
          color="primary"
        >
          Retour
        </Button>
      </Container>
    );
  }
}

const styles = (theme) => ({
  root: {
    //backgroundColor: '#020F59',
  },
  ncard: {
    width: "7vw",
    height: "5vw",
    margin: "10px",
    textAlign: "center",
    justifyContent: "center",
    backgroundColor: "#3DADF2",
  },
  ccard: {
    width: "7vw",
    height: "5vw",
    margin: "10px",
    textAlign: "center",
    justifyContent: "center",
    backgroundColor: "#3DADF2",
  },
  optsol: {
    width: "30vw",
    height: "5vw",
    margin: "10px",
    textAlign: "center",
    justifyContent: "center",
    backgroundColor: "#3DADF2",
  },
  listSol: {
    width: "100%",
    backgroundColor: theme.palette.background.paper,
    overflow: "auto",
    maxHeight: 120,
  },
  emptyheight: {
    height: "3vw",
  },
  title: {
    fontSize: 20,
    textAlign: "center",
  },
  text_contenu: {
    fontSize: 18,
  },
  text_contenu_b: {
    fontSize: 16,
  },

  pos: {
    marginBottom: 12,
  },
  textfield: {
    marginRight: 15,
    marginBottom: 20,
    backgroundColor: "#e898ac",
  },
  btn: {
    backgroundColor: "#002845",
  },
});
export default withStyles(styles)(ShowResults);

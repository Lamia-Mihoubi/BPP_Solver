import React from "react";
import './inputPage.css';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import { withStyles } from '@material-ui/core/styles';
import { Container, TextField, Button, Grid } from "@material-ui/core";
import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import ExpansionPanelSummary from "@material-ui/core/ExpansionPanelSummary";
import ExpansionPanelDetails from "@material-ui/core/ExpansionPanelDetails";
import Typography from "@material-ui/core/Typography";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import ListItem from "@material-ui/core/ListItem";
import List from "@material-ui/core/List";

class FormNC extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      n: 10,
      c: 10,
      objects: [],
    };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange1 = this.handleChange1.bind(this);
    this.handleChange2 = this.handleChange2.bind(this);
  }

  handleChange1(event) {
    this.setState({ c: event.target.value });
  }
  handleChange2(event) {
    this.setState({ n: event.target.value });
  }
  async handleSubmit(event) {
    //c'est la win nebe3tou la rqt
    //alert('Le n a été soumis : ' + this.state.n);
    event.preventDefault();
    var data = {
      n: this.state.n,
      c: this.state.c,
    };

    const response = await fetch("/random", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    const res = await response.json();

    this.setState({ objects: res.liste });
    this.props.sendpb(this.state.n, this.state.c, res.liste);
  
  }
  render() {
    const { classes } = this.props; 
    return (
     
         <Container  width={1} /*className={classes.root}*/>
          <Typography variant="h3" className={classes.pagetitle} gutterBottom>
           Générer une instance aléatoire
          </Typography>
      
                <Card width={1} className={classes.root}>
                    <CardHeader title="Entrez les paramètres de l'instance" />
                        <CardContent>
                                <form onSubmit={this.handleSubmit}>
                                    <Grid container spacing={3}>
                                      <Grid item xs={10} sm={3}>
                                        <TextField
                                          required
                                          variant="outlined"
                                          type="number"
                                          label="Nombre d'objets "
                                          size="small"
                                          value={this.state.n}
                                          onChange={this.handleChange2}
                                          InputProps={{ inputProps: { min: 1 } }}
                                        />
                                      </Grid>
                                      <Grid item xs={10} sm={3}>
                                        <TextField
                                          
                                          required
                                          variant="outlined"
                                          type="number"
                                          label="Capacité des boites "
                                          size="small"
                                          value={this.state.c}
                                          onChange={this.handleChange1}
                                          InputProps={{ inputProps: { min: 1 } }}
                                        />
                                      </Grid>

                                      <Grid item xs={12}>
                                        <Button variant="contained" color="primary" type="submit">
                                          Générer
                                        </Button>
                                      </Grid>
                                    </Grid>
                                </form>
                                  <br></br>
                                  <ExpansionPanel>
                                    <ExpansionPanelSummary
                                      expandIcon={<ExpandMoreIcon />}
                                      aria-controls="panel1a-content"
                                      id="panel1a-header"
                                    >
                                      Instance générée
                                    </ExpansionPanelSummary>
                                    <ExpansionPanelDetails>
                                      <List height={200} width={200} itemSize={46}>
                                        {this.state.objects.map((d) => {
                                          return <ListItem>{d}</ListItem>;
                                        })}
                                      </List>
                                    </ExpansionPanelDetails>
                                  </ExpansionPanel>
                          </CardContent>
                 </Card>
          </Container>
            
    );
  }
}

const styles = theme => ({
  root: {
        
    margin: theme.spacing(3),
    width: "67vw",
    marginLeft : "1cm"

  },
  
})  
export default withStyles(styles)(FormNC);

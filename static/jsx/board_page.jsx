/*
AllLists
  - List
    - ListName
    - AllCards
      - Card
*/

var AllLists = React.createClass({
  getInitialState: function() {
    return {lists: []};
  },
  loadListsFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      success: function(data) {
        this.setState({lists: data.lists});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  componentDidMount: function() {
    this.loadListsFromServer();
    setInterval(this.loadListsFromServer, this.props.pollInterval);
  },
  render: function() {
    var lists = this.state.lists.map(function(list) {
      return (
        <List key={list.id} list={list} />
      )
    });
    return (
      <div className="allLists">
        {lists}
      </div>
    )
  }
});


var List = React.createClass({
  render: function() {
    return (
      <div className="list" id={'list' + this.props.list.id}>
        <ListName list_name={this.props.list.name} list_id={this.props.list.id} />
        <AllCards url="/board3/8/" pollInterval={2000} />
      </div>
    )
  }
});


var ListName = React.createClass({
  render: function() {
    return (
      <div className="listName">
        <h4>{this.props.list_name}<span className="delete" id={'delete_list' + this.props.list_id}>&times;</span></h4>
      </div>
    )
  }
});


var AllCards = React.createClass({
  getInitialState: function() {
    return {cards: []};
  },
  loadCardsFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      success: function(data) {
        this.setState({cards: data.cards});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  componentDidMount: function() {
    this.loadCardsFromServer();
    setInterval(this.loadCardsFromServer, this.props.pollInterval);
  },
  render: function() {
    var cards = this.state.cards.map(function(card) {
      return (
        <Card key={card.id} card={card} />
      )
    });
    return (
      <div className="allCards">
        {cards}
      </div>
    )
  }
});


var Card = React.createClass({
  render: function() {
    return (
      <div className="card">
        {card.content}
      </div>
    )
  }
});


ReactDOM.render(
  <AllLists url="/board3/8/" pollInterval={2000} />,
  document.getElementById('main_board')
);

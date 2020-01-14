/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React from 'react';
import {StyleSheet, View, Text, ScrollView} from 'react-native';
import LongCard from './../includes/LongCard';

class Home extends React.Component {
  state = {
    title: 'Daily Trainings',
    subHeading: 'Keep training daily for better results',
    trainings: [
      {
        id: 1,
        title: 'Attention & Focus',
        description: 'Improve your concentration!',
        backgroundColor: '#FFF5DC',
        iconBackgroundColor: '#FFC57C',
        imageUrl: require('./../../assets/images/1.png'),
      },
      {
        id: 2,
        title: 'Activities & Vision',
        description: 'Improve your collaboration!',
        backgroundColor: '#E7F4FF',
        iconBackgroundColor: '#60A0FB',
        imageUrl: require('./../../assets/images/2.png'),
      },
      {
        id: 3,
        title: 'Activities & Vision',
        description: 'Improve your collaboration!',
        backgroundColor: '#E5F4EB',
        iconBackgroundColor: '#83D39D',
        imageUrl: require('./../../assets/images/3.png'),
      },
    ],
  };
  renderLongCard = () => {
    return this.state.trainings.map((training, index) => {
      return (
        <LongCard
          key={index}
          title={training.title}
          description={training.description}
          backgroundColor={training.backgroundColor}
          iconBackgroundColor={training.iconBackgroundColor}
          imageUrl={training.imageUrl}
        />
      );
    });
  };
  render() {
    return (
      <ScrollView contentContainerStyle={styles.mainContainer}>
        <View style={styles.containerHead}>
          <Text style={styles.title}>{this.state.title}</Text>
          <Text style={styles.subHeading}>{this.state.subHeading}</Text>
        </View>

        <View>{this.renderLongCard()}</View>
      </ScrollView>
    );
  }
}

const styles = StyleSheet.create({
  mainContainer: {
    padding: 20,
  },
  containerHead: {
    marginVertical: 25,
  },
  title: {
    color: '#000',
    textAlign: 'center',
    fontSize: 35,
    fontWeight: 'bold',
    marginBottom: 12,
  },
  subHeading: {
    textAlign: 'center',
    fontSize: 15,
  },
});
export default Home;

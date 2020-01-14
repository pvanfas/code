/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React from 'react';
import {StyleSheet, View, Text, TouchableOpacity, Image} from 'react-native';
import Icon from 'react-native-vector-icons/dist/MaterialIcons';

class LongCard extends React.Component {
  state = {};

  render() {
    let {
      title,
      description,
      backgroundColor,
      iconBackgroundColor,
      imageUrl,
    } = this.props;

    return (
      <TouchableOpacity
        activeOpacity={0.9}
        style={[styles.card, {backgroundColor: backgroundColor}]}>
        <View style={styles.cardLeft}>
          <View style={styles.cardLeftTopContainer}>
            <Text style={styles.cardHead}>{title}</Text>
            <Text style={styles.cardText}>{description}</Text>
          </View>
          <View style={styles.cardLeftBottomContainer}>
            <View
              style={[styles.circle, {backgroundColor: iconBackgroundColor}]}>
              <Icon name="check" color="#fff" size={25} />
            </View>
            <View
              style={[styles.circle, {backgroundColor: iconBackgroundColor}]}>
              <Icon name="check" color="#fff" size={25} />
            </View>
            <View
              style={[styles.circle, {backgroundColor: iconBackgroundColor}]}>
              <Icon name="check" color="#fff" size={25} />
            </View>
            <View
              style={[styles.circle, {backgroundColor: iconBackgroundColor}]}>
              <Icon name="check" color="#fff" size={25} />
            </View>
          </View>
        </View>
        <View style={styles.cardRight}>
          <Image style={styles.image} source={imageUrl} />
        </View>
      </TouchableOpacity>
    );
  }
}

const styles = StyleSheet.create({
  card: {
    paddingVertical: 30,
    paddingHorizontal: 20,
    borderRadius: 35,
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginBottom: 10,
  },
  cardLeft: {},
  cardLeftTopContainer: {
    marginBottom: 20,
  },
  cardLeftBottomContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
  },
  cardHead: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'left',
    marginBottom: 8,
  },
  cardText: {
    textAlign: 'left',
  },
  cardRight: {
    flexDirection: 'row',
    textAlign: 'center',
    width: '30%',
  },
  circle: {
    width: 37,
    height: 37,
    borderRadius: 35,
    justifyContent: 'center',
    alignItems: 'center',
    marginEnd: 10,
  },
  icon: {
    color: '#fff',
    fontSize: 15,
    fontWeight: 'bold',
  },
  image: {
    width: '100%',
    alignSelf: 'center',
  },
});
export default LongCard;

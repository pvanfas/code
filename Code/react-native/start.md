# Create native apps for Android and iOS using React

[![CircleCI](https://img.icons8.com/officel/30/000000/doc.png)](https://facebook.github.io/react-native/docs/getting-started)


#### *React Native combines the best parts of native development with React, a best-in-class JavaScript library for building user interfaces.*.

Starting a new react-native app
```
npx react-native init AwesomeProject
```
```
cd AwesomeProject
npx react-native run-android
```
start another teminal on project directory and apply the command
```
react-native start
```


# Navigation

```
npm install react-native-gesture-handler react-native-reanimated react-native-screens react-native-safe-area-context
npm install react-navigation-stack @react-native-community/masked-view
```

Add the following two lines to dependencies section in android/app/build.gradle:

```
implementation 'androidx.appcompat:appcompat:1.1.0-rc01'
implementation 'androidx.swiperefreshlayout:swiperefreshlayout:1.1.0-alpha02'
```

To finalize installation of react-native-gesture-handler for Android, make the following modifications to MainActivity.java:

```
package com.reactnavigation.example;

import com.facebook.react.ReactActivity;
+ import com.facebook.react.ReactActivityDelegate;
+ import com.facebook.react.ReactRootView;
+ import com.swmansion.gesturehandler.react.RNGestureHandlerEnabledRootView;

public class MainActivity extends ReactActivity {

  @Override
  protected String getMainComponentName() {
    return "Example";
  }

+  @Override
+  protected ReactActivityDelegate createReactActivityDelegate() {
+    return new ReactActivityDelegate(this, getMainComponentName()) {
+      @Override
+      protected ReactRootView createRootView() {
+        return new RNGestureHandlerEnabledRootView(MainActivity.this);
+      }
+    };
+  }
}

```
Then add the following at the top of your entry file, such as index.js or App.js:

```
import 'react-native-gesture-handler';
```

Home page

```
import React from 'react';
import {} from 'react-native';
import Home from './components/screens/Home';
import About from './components/screens/About';
import 'react-native-gesture-handler';
import {createAppContainer} from 'react-navigation';
import {createStackNavigator} from 'react-navigation-stack';

class App extends React.Component {
  state = {};
  render() {
    return <AppContainer />;
  }
}

const AppNavigator = createStackNavigator({
  Home: {
    screen: Home,
  },
  About: {
    screen: About,
  },
});

const AppContainer = createAppContainer(AppNavigator);

export default App;

```
About page

```
import React from 'react';
import {View, Text, StyleSheet} from 'react-native';

class About extends React.Component {
  render() {
    return (
      <View style={styles.page}>
        <Text>About Screen</Text>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  page: {flex: 1, alignItems: 'center', justifyContent: 'center'},
});

export default About;

```

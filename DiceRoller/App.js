import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, View } from 'react-native';
import { useFonts } from 'expo-font';

export default function App() {
  // Fonts
  const [fontsLoaded] = useFonts({
    'Jersey15Charted-Regular': require('./assets/fonts/Jersey15Charted-Regular.ttf')
  })

  if (!fontsLoaded) {
    return null;
  }
  

/* ---------------------------------- Page ---------------------------------- */

  return (
    <View style={page.container}>
      <View style={page.title_container}>
        <Text style={title.title}>Dice Roller</Text>
        <StatusBar style="auto" />
      </View>
      {/* <View style={page.empty}></View> */}
      <View style={page.button_container}>
        <Button title='Start'/>
      </View>
    </View>
  );
}

/* --------------------------------- Styling -------------------------------- */

const page = StyleSheet.create({
  container: {
    flex:1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'space-evenly',
    paddingTop:150,
    // marginBottom: 200
  },

  title_container: {
    flex:0.75,
    borderColor: 'black',
    borderWidth: 5,
    fontFamily: 'Jersey15Charted-Regular',
    fontSize: 70
  },

  button_container: {
    flex:2,
    borderWidth:5,
    height:200,
    justifyContent: 'center'
  }
});

const title = StyleSheet.create({
  title: {
    fontFamily: 'Jersey15Charted-Regular',
    fontSize: 70
  }
})
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
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
      <Text style={title.title}>Dice Roller</Text>
      <StatusBar style="auto" />
    </View>
  );
}

/* --------------------------------- Styling -------------------------------- */

const page = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

const title = StyleSheet.create({
  title: {
    fontFamily: 'Jersey15Charted-Regular',
    fontSize: 70
  }
})
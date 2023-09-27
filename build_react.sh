pushd ./aoc-android-frontend
npm run build
popd
cp -r ./aoc-android-frontend/build ./backend/build
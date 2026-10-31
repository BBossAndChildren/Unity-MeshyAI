import {fileURLToPath} from 'node:url';
// Reuse the repository's already installed dependencies without network calls.
const installed=name=>fileURLToPath(new URL('../../office-ten-tools/node_modules/'+name,import.meta.url));
export default {base:'./',resolve:{alias:[{find:/^react$/,replacement:installed('react/index.js')},{find:/^react\/jsx-runtime$/,replacement:installed('react/jsx-runtime.js')},{find:/^react-dom\/client$/,replacement:installed('react-dom/client.js')}]},build:{outDir:'dist-v001',emptyOutDir:false}};
